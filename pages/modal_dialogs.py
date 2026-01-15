from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.modal_btn = WebElement(driver, 'button.btn.btn-primary')
        self.icon_el = WebElement(driver, '#app > header > a > img')
        self.btn_small = WebElement(driver, '#showSmallModal')
        self.btn_large = WebElement(driver, '#showLargeModal')
        self.modal_small = WebElement(driver, 'body > div.fade.modal.show')
        self.modal_large = WebElement(driver, 'body > div.fade.modal.show')
        self.btn_small_close = WebElement(driver, '#closeSmallModal')
        self.btn_large_close = WebElement(driver, '#closeLargeModal')
