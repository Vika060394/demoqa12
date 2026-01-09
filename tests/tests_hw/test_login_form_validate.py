import time
from pages.form_page import FormPage

def test_login_form_validate(browser):
    login_form = FormPage(browser)

    login_form.visit()
    assert login_form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert login_form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert login_form.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert login_form.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    login_form.btn_submit.scroll_to_element()
    login_form.btn_submit.click()
    assert login_form.form_validated.get_dom_attribute('class') == 'was-validated'

