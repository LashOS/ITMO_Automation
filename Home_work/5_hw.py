
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, "#user-name")
if username is None:
    print("Элемент не найден")
else:
    print("Элемент найден")

password = driver.find_element(By.CSS_SELECTOR, "#password")
if password is None:
    print("Элемент не найден")
else:
    print("Элемент найден")

login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
if login_button is None:
    print("Элемент не найден")
else:
    print("Элемент найден")

    # login-button
