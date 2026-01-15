# from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa
# import time

def test_check_icon(browser):
    # driver = webdriver.Chrome()
    # browser.get("https://demoqa.com/")
    #
    # icon = browser.find_element(By.CSS_SELECTOR, '"#app>header>a"')
    #
    # if icon is None:
    #   print('Не найден')
    # else:
    #   print('Найден')

    # создаем объект класса и передаем browser
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    # time.sleep(3)
    demo_qa_page.icon.click()
    # time.sleep(3)
    assert demo_qa_page.equal_url()
    # вызываем assert, проверяем что элемент есть на стр
    assert demo_qa_page.icon.exist()



