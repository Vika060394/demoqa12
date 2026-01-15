import time
from pages.tables import Tables

def test_tables(browser):
    page_tables = Tables(browser)

    # проверка блока no rows found
    # assert not page_tables.no_data.exist()
    # # удаляем все записи
    # while page_tables.btn_delete_row.exists():
    # page_tables.btn_delete_row.click()
    # time.sleep(2)
    # assert page_tables.no_data.exist()

    # тест 1 дз 11
    page_tables.visit()
    page_tables.btn_add.click()
    page_tables.reg_form.exist()
    page_tables.btn_submit.click()
    page_tables.reg_form.exist()

    page_tables.first_name.send_keys('Jo')
    page_tables.last_name.send_keys('Iv')
    page_tables.user_email.send_keys('11@f.fd')
    page_tables.age.send_keys('20')
    page_tables.salary.send_keys('30')
    page_tables.department.send_keys('10')
    time.sleep(2)
    page_tables.btn_submit.click()
    assert not page_tables.reg_form.exist()

    reg_form4 = ['Jo', 'Iv', '11@f.fd', '20', '30', '10']
    for item in reg_form4:
        assert item in page_tables.web_tables.get_text()

    page_tables.click_pen.click()
    time.sleep(2)

    assert page_tables.reg_form.exist()
    assert page_tables.first_name.get_dom_attribute('value') == 'Jo'
    assert page_tables.last_name.get_dom_attribute('value') == 'Iv'
    assert page_tables.user_email.get_dom_attribute('value') == '11@f.fd'
    assert page_tables.age.get_dom_attribute('value') == '20'
    assert page_tables.salary.get_dom_attribute('value') == '30'
    assert page_tables.department.get_dom_attribute('value') == '10'

    page_tables.first_name.clear()
    time.sleep(2)
    page_tables.first_name.send_keys('Tom')
    time.sleep(2)
    page_tables.btn_submit.click()
    assert not page_tables.reg_form.exist()
    time.sleep(2)
    new_name = 'Tom'
    reg_form = page_tables.web_tables.get_text()
    assert new_name in reg_form
    time.sleep(2)

    page_tables.click_basket4.click()
    assert "Tom" not in page_tables.web_tables.get_text()

#     тест кейс 2 дз 11

    page_tables.visit()

    current_value = page_tables.select_rows.get_dom_attribute('value')

    if current_value != '5':
        page_tables.select_rows.scroll_to_element()
        page_tables.select_rows.click()
        time.sleep(1)
        page_tables.btn_5_rows.click()
        time.sleep(2)

    assert page_tables.btn_next.get_dom_attribute('disabled') is not None
    assert page_tables.btn_previous.get_dom_attribute('disabled') is not None

    page_tables.btn_add.click()
    time.sleep(2)
    page_tables.first_name.send_keys('John')
    page_tables.last_name.send_keys('Doe')
    page_tables.user_email.send_keys('gg@gg.com')
    page_tables.age.send_keys('23')
    page_tables.salary.send_keys('23')
    page_tables.department.send_keys('23')
    page_tables.btn_submit.click()
    time.sleep(1)

    page_tables.btn_add.click()
    page_tables.first_name.send_keys('John')
    page_tables.last_name.send_keys('Doe')
    page_tables.user_email.send_keys('gg@gg.com')
    page_tables.age.send_keys('23')
    page_tables.salary.send_keys('23')
    page_tables.department.send_keys('23')
    page_tables.btn_submit.click()
    time.sleep(1)

    page_tables.btn_add.click()
    page_tables.first_name.send_keys('John')
    page_tables.last_name.send_keys('Doe')
    page_tables.user_email.send_keys('gg@gg.com')
    page_tables.age.send_keys('23')
    page_tables.salary.send_keys('23')
    page_tables.department.send_keys('23')
    page_tables.btn_submit.click()
    time.sleep(1)

    page_tables.btn_next.click()
    assert page_tables.page_info2.get_dom_attribute('value') == '2'

    page_tables.btn_previous.click()
    assert page_tables.page_info1.get_dom_attribute('value') == '1'







