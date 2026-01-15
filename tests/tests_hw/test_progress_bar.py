from pages.base_page import BasePage
from pages.progress_bar import ProgressBar
import time

def test_progress_bar(browser):
    page = ProgressBar(browser)

    page.visit()
    time.sleep(1)

    page.button.click()

    while True:
        if page.bar.get_dom_attribute('aria-valuenow') == '51':
            page.button.click()
            break
    time.sleep(1)