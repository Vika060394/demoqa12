import time
from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
import pytest

# def test_seo_meta():
#     browser.switch_to.window(browser.window_handles[0])

@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(1)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width, initial-scale=1'