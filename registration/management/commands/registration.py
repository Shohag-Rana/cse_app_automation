from django.core.management.base import BaseCommand
import time
from config import USER_EMAIL, PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument("id", nargs="+", type=int)

    def handle(self, *args, **options):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://beta.mbstucseaa.org/login")
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(USER_EMAIL)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
        button = driver.find_element(By.XPATH, '//form/div[3]/div[2]/button')
        button.click()
        time.sleep(10)
