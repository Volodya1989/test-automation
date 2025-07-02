# conftest.py

pytest_plugins = []

import os
import shutil
import pytest
from pathlib import Path
from configs.config import BASE_URL
from helpers.auth import login


@pytest.fixture(scope="session")
def storage_state(tmp_path_factory, browser):
    context = browser.new_context()
    page = context.new_page()
    login(page, BASE_URL, "test@123.com", "123456")
    storage_file = tmp_path_factory.mktemp("data") / "storage.json"
    context.storage_state(path=str(storage_file))
    page.close()
    context.close()
    return str(storage_file)


@pytest.fixture(scope="function")
def auth_page(browser, storage_state, request):
    temp_video_dir = Path("videos/tmp")
    temp_video_dir.mkdir(parents=True, exist_ok=True)

    context = browser.new_context(
        storage_state=storage_state,
        record_video_dir=str(temp_video_dir)
    )
    page = context.new_page()

    yield page

    test_name = request.node.name.replace("/", "_")
    context.close()
    if page.video:
        video_path = page.video.path()
        final_path = Path("videos") / f"{test_name}.webm"
        final_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(video_path, final_path)
