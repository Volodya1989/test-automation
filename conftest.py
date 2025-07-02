import os
import shutil
import pytest
from pathlib import Path

@pytest.fixture(scope="function")
def context(browser, request):
    # Use a temp directory to store videos initially
    temp_video_dir = Path("videos/tmp")
    temp_video_dir.mkdir(parents=True, exist_ok=True)

    context = browser.new_context(record_video_dir=str(temp_video_dir))
    page = context.new_page()

    yield page  # <-- Run the test

    # Save video using the test function name
    test_name = request.node.name.replace("/", "_")
    video_path = page.video.path()
    final_path = Path("videos") / f"{test_name}.webm"
    final_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(video_path, final_path)

    context.close()
