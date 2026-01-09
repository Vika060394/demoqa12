from pages.text_box import TextBox
from components.components import WebElement
import time

def test_text_box(browser):
    text_box = TextBox(browser)

    name = 'Tester'
    address = 'Address'

    text_box.visit()
    text_box.name.send_keys(name)
    time.sleep(2)
    text_box.address.send_keys(address)
    time.sleep(2)
    text_box.btn_submit.scroll_to_element()
    text_box.btn_submit.click()

    assert text_box.output_name.get_text() == 'Name:' + name
    # assert text_box.output_address.get_text() == 'Current Address :' + address





