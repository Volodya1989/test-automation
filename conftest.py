import os
import shutil
import pytest
from pathlib import Path
from configs.config import BASE_URL
from helpers.auth import login

VIDEO_DIR = Path("videos")
TMP_VIDEO_DIR = VIDEO_DIR / "tmp"

@pytest.fixture(scope="session")
def storage_state(tmp_path_factory, browser):
    """Login once, persist storage."""
    context = browser.new_context()
    page = context.new_page()
    login(page, BASE_URL, "test@123.com", "123456")

    storage_file = tmp_path_factory.mktemp("data") / "storage.json"
    context.storage_state(path=str(storage_file))
    context.close()
    return str(storage_file)

@pytest.fixture(scope="function")
def auth_page(browser, storage_state, request):
    """Create a new context per test using stored login session."""
    TMP_VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    context = browser.new_context(
        storage_state=storage_state,
        record_video_dir=str(TMP_VIDEO_DIR)
    )
    page = context.new_page()

    yield page  # Test executes here

    # Save video only if test failed
    if request.node.rep_call.failed:
        test_name = request.node.name.replace("/", "_")
        if page.video:
            video_path = page.video.path()
            final_path = VIDEO_DIR / f"{test_name}.webm"
            final_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(video_path, final_path)

    page.close()
    context.close()

# Hook to check test result
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
