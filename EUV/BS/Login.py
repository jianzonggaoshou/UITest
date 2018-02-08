# coding:utf-8
from selenium.webdriver.common.by import By


class Login:
    def __init__(self):
        pass

    @staticmethod
    def inspection_team_leader_login(driver, username, password):
        driver.find_element(By.ID, "userName").clear()
        driver.find_element(By.ID, "userName").send_keys(username)
        driver.find_element(By.ID, "userPwd").clear()
        driver.find_element(By.ID, "userPwd").send_keys(password)
        driver.find_element(By.CLASS_NAME, "submit").click()
