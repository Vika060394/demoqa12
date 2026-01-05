from components.components import WebElement
from pages.base_page import BasePage

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.accordian_el = WebElement(driver, '#section1Content > p')
        self.accordian_el2 = WebElement(driver, '#section1Heading')
        self.answer1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.answer2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.answer3 = WebElement(driver, '#section3Content > p')