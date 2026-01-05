from components.components import WebElement
from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.accordian_el.visible()
    accordion_page.accordian_el2.click()
    time.sleep(2)
    assert not accordion_page.accordian_el.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.answer1.visible()
    assert not accordion_page.answer2.visible()
    assert not accordion_page.answer3.visible()

