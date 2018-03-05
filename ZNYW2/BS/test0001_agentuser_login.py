# coding:utf-8
import unittest
from selenium import webdriver
from time import sleep
from LoginPage import LoginPage


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LoginPage.testUrl)

    def test_case(self):
        """测试登录：代理商agentuser"""
        self.driver.implicitly_wait(20)
        LoginPage.login(self.driver, username="agentxuzhen", password="123456")
        # self.assertEqual()

    def tearDown(self):
        sleep(100)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
