import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
driver.get("https://www.google.com")
print(driver.title)
pageback = driver.back()
print(driver.title)
driver.forward()
print(driver.title)