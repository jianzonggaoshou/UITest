# coding:utf-8
from selenium.webdriver.common.by import By
from time import sleep


class InforME:

    """添加设备定位元素"""
    # 信息管理定位
    navInformationManagementLocation = By.XPATH
    # 信息管理按钮
    navInformationManagementButton = "//a[text()='信息管理']"

    # 台账管理定位
    equipmentManagementLocation = By.XPATH
    # 台账管理按钮
    equipmentManagementButton = "//div[contains(text(),'台账管理')]"

    # 对应配电室树定位
    roomLocation = By.XPATH
    # 对应配电室树
    roomTree = '//*[@id="informationManagerMain"]/div[1]/div[2]/div[4]/div[1]/div[2]/ul/li/ul[1]/li/ul[1]/li/span[2]'

    # 新增按钮定位
    addEquipmentLocation = By.XPATH
    # 新增按钮
    addEquipmentButton = '//button[text()="新增"]'

    def __init__(self):
        pass

    @staticmethod
    def add(driver):
        driver.find_element(InforME.navInformationManagementLocation, InforME.navInformationManagementButton).click()
        driver.find_element(InforME.equipmentManagementLocation, InforME.equipmentManagementButton).click()
        sleep(15)
        driver.find_element(InforME.roomLocation, InforME.roomTree).click()
        sleep(3)
        driver.find_element(InforME.addEquipmentLocation, InforME.addEquipmentButton).click()



