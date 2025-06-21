from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)

usename_input = driver.find_element(By.NAME, "username").send_keys("Admin")
password_input = driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(5)

#login_button = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
#login_button.click()

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
dashboard_text = driver.find_element(By.XPATH,"//h6[text()='Dashboard']")
assert dashboard_text.text == 'Dashboard'
