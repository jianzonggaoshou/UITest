# coding:utf-8
from selenium.webdriver.common.by import By
from time import sleep


class Login:
    def __init__(self):
        pass

    @staticmethod
    def login(driver, username, password):
        driver.find_element(By.ID, "com.sito.evpro.inspection.dev:id/edit_username").clear()
        driver.find_element(By.ID, "com.sito.evpro.inspection.dev:id/edit_username").send_keys(username)
        driver.find_element(By.ID, "com.sito.evpro.inspection.dev:id/edit_password").clear()
        driver.find_element(By.ID, "com.sito.evpro.inspection.dev:id/edit_password").send_keys(password)
        driver.find_element(By.ID, "com.sito.evpro.inspection.dev:id/tv_login").click()