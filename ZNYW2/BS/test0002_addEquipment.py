# coding:utf-8
import unittest
from selenium import webdriver
from time import sleep
from LoginPage import LoginPage
from InforManagementEquipmentPage import InforME


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LoginPage.testUrl)

    def test_case(self):
        """测试添加设备：代理商agentuser"""
        self.driver.implicitly_wait(20)
        LoginPage.login(self.driver, username="agentxuzhen", password="123456")
        self.driver.implicitly_wait(20)
        InforME.add(self.driver)


    def tearDown(self):
        sleep(20)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
