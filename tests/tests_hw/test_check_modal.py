from pages.modal_dialogs import ModalDialogs
import time
import pytest



@pytest.mark.skipif(True, reason='страница не доступна')
def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    assert modal_dialogs.btn_small.exist()
    assert modal_dialogs.btn_large.exist()

    modal_dialogs.btn_small.click()
    time.sleep(1)
    assert modal_dialogs.modal_small.exist()
    modal_dialogs.btn_small_close.click()
    assert not modal_dialogs.modal_small.exist()


    modal_dialogs.btn_large.click()
    time.sleep(1)
    assert modal_dialogs.modal_large.exist()
    modal_dialogs.btn_large_close.click()
    assert not modal_dialogs.modal_large.exist()

