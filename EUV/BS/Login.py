# coding:utf-8
from selenium.webdriver.common.by import By
from time import sleep


class Login:
    def __init__(self):
        pass

    @staticmethod
    def login(driver, username, password):
        driver.find_element(By.ID, "userName").clear()
        driver.find_element(By.ID, "userName").send_keys(username)
        driver.find_element(By.ID, "userPwd").clear()
        driver.find_element(By.ID, "userPwd").send_keys(password)
        driver.find_element(By.CLASS_NAME, "submit").click()
