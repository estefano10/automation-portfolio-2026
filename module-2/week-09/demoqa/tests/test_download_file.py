from pages.upload_download_page import UploadDownloadPage
from playwright.sync_api import Page, expect

def test_download_file(page: Page, tmp_path):
    upload_download = UploadDownloadPage(page)
    upload_download.open()
    down = upload_download.download_file()
    assert down.suggested_filename == "sampleFile.jpeg"
    dest = tmp_path / down.suggested_filename
    down.save_as(dest)
    assert dest.exists()