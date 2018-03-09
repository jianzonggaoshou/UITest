# coding:utf-8
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from LoginPage import LoginPage


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
        # 点击信息管理
        self.driver.find_element(By.XPATH, '//a[@href="#/informationManager/informationManagerMain"]').click()
        self.driver.implicitly_wait(20)
        # 点击台账管理
        self.driver.find_element(By.XPATH, '//div[contains(text(), "台账管理")]').click()
        sleep(3)
        # 点击左侧配电室
        self.driver.find_element(By.XPATH, '//span[contains(text(), "低压配电室")]').click()
        # 点击新增按钮
        self.driver.find_element(By.XPATH, '//*[@id="informationManagerMain"]/div[1]/div[2]/div[4]/div[2]/ul[1]/li[4]/button').click()
        sleep(1)
        # 输入设备名称
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入设备名称"]').send_keys("1212")
        # 点击电压级别
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="informationManagerMain"]/div[2]/div[4]/div[2]/div[2]/div/div/div[1]/input[2]').click()
        sleep(1)
        # 默认选择第一个
        self.driver.find_element(By.XPATH, '//*[@id="informationManagerMain"]/div[2]/div[4]/div[2]/div[2]/div/div/div[2]/ul[2]/li[1]').click()
        # 点击设备类型
        sleep(1)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请选择设备类型"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//li[contains(text(), "变压器")]').click()
        # 点击投运时间

        # 点击保存

    def tearDown(self):
        sleep(20)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
