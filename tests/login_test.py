
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

class Test_Login():
    def test_login(self, method):
        usename_input = self.driver.find_element(By.NAME, "username").send_keys("Admin")
        password_input = self.driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
        dashboard_text = self.driver.find_element(By.XPATH,"//h6[text()='Dashboard']")
        assert dashboard_text.text == 'Dashboard'
