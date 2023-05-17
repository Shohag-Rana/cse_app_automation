import time

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create your tests here.
def test_user_registration():
    driver = webdriver.Chrome()
    driver.get("https://beta.mbstucseaa.org/login")
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("admin@example.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    button = driver.find_element(By.XPATH, '//form/div[3]/div[2]/button')
    button.click()
    time.sleep(10)


