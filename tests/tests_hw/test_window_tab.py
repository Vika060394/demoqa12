import time
from pages.window_tab import Window

def test_window_tab(browser):
    window = Window(browser)
    window.visit()

    assert window.link_home.exist()
    assert window.link_home.get_text() == 'Home'
    assert window.link_home.get_dom_attribute('href') == 'https://demoqa.com'

    assert len(browser.window_handles) == 1
    window.link_home.click_force()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)


