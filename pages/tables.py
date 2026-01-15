from components.components import WebElement
from pages.base_page import BasePage

class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement (driver, 'div.rt-noData')
        self.btn_delete_row = WebElement (driver, "span[title='Delete']")
        self.btn_add = WebElement (driver, "#addNewRecordButton")
        self.reg_form = WebElement (driver, 'body > div.fade.modal.show')
        self.btn_submit = WebElement (driver, "#submit")
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.web_tables = WebElement(driver, ".rt-tbody")
        self.row_tables = WebElement(driver, ".rt-tbody .rt-tr-group")

        self.click_pen = WebElement (driver, "#edit-record-4 > svg")
        self.click_basket4 = WebElement (driver, "#delete-record-4 > svg > path")

        self.btn_next = WebElement (driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button")
        self.btn_previous = WebElement (driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button")
        self.page_info = WebElement (driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo")
        self.page_info1 = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')
        self.page_info2 = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')
        self.select_rows = WebElement (driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select")
        self.btn_5_rows = WebElement (driver, "option[value='5']")


        self.column_name = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1)')
        self.column_lastName = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(2)')
        self.column_age = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(3) > div.rt-resizable-header-content')
        self.column_email = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(4) > div.rt-resizable-header-content')
        self.column_salary = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(5) > div.rt-resizable-header-content')
        self.column_department = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(6) > div.rt-resizable-header-content')
        self.column_action = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(7) > div.rt-resizable-header-content')

