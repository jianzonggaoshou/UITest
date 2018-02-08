# coding:utf-8
import unittest
from selenium import webdriver
from time import sleep
from Login import Login


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://172.16.40.240:8080/sitopeuv/")

    def test_case(self):
        """测试登录：巡检组长"""
        Login.inspection_team_leader_login(self.driver, username="13630241183", password="13630241183")

    def tearDown(self):
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
