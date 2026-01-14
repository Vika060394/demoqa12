from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_elements(By.ID, "user-name")
password = driver.find_elements(By.ID, "password")
submit = driver.find_elements(By.ID, "login-button")
if username and password and submit:
    print("Элементы найдены")
else:
    print("Элементы не найдены")