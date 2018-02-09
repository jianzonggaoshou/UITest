# coding:utf-8
from selenium.webdriver.common.by import By
from time import sleep


class CompanyNoticePage:
    def __init__(self):
        pass

    @staticmethod
    def add_company_notice(driver, a):
        driver.find_element(By.ID, "buttonToAdd").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/index-header/div/div[3]/div[2]/business-notice/div[2]/div/form/div[1]/input").sendkeys(a)
