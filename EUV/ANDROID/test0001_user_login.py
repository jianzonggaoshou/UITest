# coding=utf-8
import unittest
from appium import webdriver
from time import sleep
from Login import Login


class Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1.1',
                        'deviceName': 'Android Emulator',
                        'appPackage': 'com.sito.evpro.inspection.dev',
                        'appActivity': 'com.sito.evpro.inspection.view.splash.SplashActivity',
                        'noReset': True,
                        'unicodeKeyboard': True,
                        'resetKeyboard': True}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_case(self):
        """测试登录：13630241183"""
        sleep(3)
        Login.login(self.driver, username="13630241183", password="13630241183")

    def tearDown(self):
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

