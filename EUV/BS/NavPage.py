# coding:utf-8
from selenium.webdriver.common.by import By
from time import sleep


class NavPage:
    def __init__(self):
        pass

    @staticmethod
    def nav_company_notice_click(driver):
        driver.find_element(By.XPATH, "//div[text()='企业通知']/preceding-sibling::i").click()
