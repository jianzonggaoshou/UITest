# coding:utf-8
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self):
        pass

    @staticmethod
    def type_my_work(driver):
        driver.find_element(By.ID, 'com.sito.evpro.inspection.dev:id/tv_repair').click()

    @staticmethod
    def type_failure_to_report(driver):
        driver.find_element(By.ID, '').click()

    def type