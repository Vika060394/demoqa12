from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    page_dialogs = ModalDialogs(browser)
    page_dialogs.visit()

    assert page_dialogs.modal_btn.check_count_elements(count=2)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.icon_el.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
