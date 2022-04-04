import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tuitions:
    # Tuitions
    lnkTutions_name = "Tuitions"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/button"

    txtTitle_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/input"

    radiobtnType = "(//input[@name='type'])[2]"

    drpOpenSyllabus_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div"
    drpSelectSyllsbus_xpath = "//div[@id='menu-syllabus_id']/div[3]/ul/li[4]"

    drpOpenClass_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div"
    drpSelectClass_xpah = "//div[@id='menu-class_id']/div[3]/ul/li[2]"

    drpOpenSubject_xpath = "/html/body/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-subject_id']/div[3]/ul/li[2]"

    drpOpenMode_xpath = "/html/body/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div"
    drpSelectMode_xpath = "//div[@id='menu-mode_of_teaching']/div[3]/ul/li[3]"

    txtCost_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/input"

    txtStartDate_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[2]/div/div/input"
    txtEndDate_xpath = "/html/body/div[2]/div/div/div[2]/form/div[5]/div[1]/div/div/input"

    uploadImage_xpath = "//input[@name='image_name']"

    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"

    chckSchedule_xpath = "//tr[4]/td[2]/div/div/div/li/div/label/span/span/input"

    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[12]/div/div[1]/button"

    txtSearch_xpath = "//div[@id='root']/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/input"
    btnSearch_xpath = "(//button[@type='button'])[4]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTuitionsMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkTutions_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def setTitle(self, textbook):
        self.driver.find_element(By.XPATH, self.txtTitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtTitle_xpath).send_keys(textbook)

    def selectType(self):
        self.driver.find_element(By.XPATH, self.radiobtnType).click()

    def drpSyllabus(self):
        self.driver.find_element(By.XPATH, self.drpOpenSyllabus_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSyllsbus_xpath).click()

    def drpClass(self):
        self.driver.find_element(By.XPATH, self.drpOpenClass_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectClass_xpah).click()

    def drpSubject(self):
        self.driver.find_element(By.XPATH, self.drpOpenSubject_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSubject_xpath).click()

    def drpMode(self):
        self.driver.find_element(By.XPATH, self.drpOpenMode_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectMode_xpath).click()

    def setCost(self, tuitions):
        self.driver.find_element(By.XPATH, self.txtCost_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCost_xpath).send_keys(tuitions)

    def setStartDate(self, tuitions):
        self.driver.find_element(By.XPATH, self.txtStartDate_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtStartDate_xpath).send_keys(tuitions)

    def setEndDate(self, tuitions):
        self.driver.find_element(By.XPATH, self.txtEndDate_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEndDate_xpath).send_keys(tuitions)

    def setTuitionImage(self, tuitions):
        self.driver.find_element(By.XPATH, self.uploadImage_xpath).clear()
        self.driver.find_element(By.XPATH, self.uploadImage_xpath).send_keys(tuitions)

    def setDescription(self, tuitions):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(tuitions)

    def CheckSchedule(self):
        self.driver.find_element(By.XPATH, self.chckSchedule_xpath).click()

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchTuition(self, tuition):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(tuition)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
