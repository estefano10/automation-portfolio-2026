from playwright.sync_api import Page, expect
from pages.upload_download_page import UploadDownloadPage

def test_upload_file(page: Page, tmp_path):
    file = tmp_path / "sampleFile.txt"
    file.write_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vel est id nisl dapibus porta eget non dolor. Phasellus vitae massa ipsum. Suspendisse sem neque, pharetra non felis eget, semper dictum ex. Ut molestie venenatis nunc a pulvinar. Integer nec euismod lectus. Aliquam tellus diam, finibus at eros sed, accumsan pulvinar velit. Suspendisse ac nulla quis nunc efficitur sagittis ac vel sapien.")
    upload = UploadDownloadPage(page)
    upload.open()
    upload.upload_file(file)
    expect(upload.uploaded_file_path).to_contain_text(file.name)