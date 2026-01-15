import time
from pages.tables import Tables


def test_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()

    page_tables.column_name.click_force()
    page_tables.column_lastName.click_force()
    page_tables.column_age.click_force()
    page_tables.column_email.click_force()
    page_tables.column_salary.click_force()
    page_tables.column_department.click_force()

    assert '-sort-asc' or '-sort-desc' in page_tables.column_name.get_dom_attribute('class')
    assert '-sort-asc' or '-sort-desc' in page_tables.column_lastName.get_dom_attribute('class')
    assert '-sort-asc' or '-sort-desc' in page_tables.column_age.get_dom_attribute('class')
    assert '-sort-asc' or '-sort-desc' in page_tables.column_email.get_dom_attribute('class')
    assert '-sort-asc' or '-sort-desc' in page_tables.column_salary.get_dom_attribute('class')
    assert '-sort-asc' or '-sort-desc' in page_tables.column_department.get_dom_attribute('class')

