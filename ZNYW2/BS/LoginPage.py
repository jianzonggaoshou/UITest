# coding:utf-8
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage:

    """定位元素"""
    # 测试网址
    testUrl = "http://39.107.121.205:8080/"

    # 用户名输入定位
    userInputLocation = By.CLASS_NAME
    # 用户名输入
    userInput = "userName"

    # 密码输入定位
    passwordInputLocation = By.CLASS_NAME
    # 密码输入
    passwordInput = "userPwd"

    # 提交按钮定位
    submitLocation = By.CLASS_NAME
    # 提交按钮
    submit = "loginRegister"

    def __init__(self):
        pass

    @staticmethod
    def login(driver, username, password):
        driver.find_element(LoginPage.userInputLocation, LoginPage.userInput).clear()
        driver.find_element(LoginPage.userInputLocation, LoginPage.userInput).send_keys(username)
        driver.find_element(LoginPage.passwordInputLocation, LoginPage.passwordInput).clear()
        driver.find_element(LoginPage.passwordInputLocation, LoginPage.passwordInput).send_keys(password)
        driver.find_element(LoginPage.submitLocation, LoginPage.submit).click()
