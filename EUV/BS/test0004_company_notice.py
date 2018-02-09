# coding:utf-8
import unittest
from selenium import webdriver
from time import sleep
from Login import Login
from NavPage import NavPage
from CompanyNoticePage import CompanyNoticePage


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://172.16.40.240:8080/sitopeuv/")

    def test_case(self):
        """测试企业通知：13630241183"""
        Login.login(self.driver, username="13630241183", password="13630241183")
        sleep(3)
        NavPage.nav_company_notice_click(self.driver)
        sleep(1)
        CompanyNoticePage.add_company_notice(self.driver, a="123")

    def tearDown(self):
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
