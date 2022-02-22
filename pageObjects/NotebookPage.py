import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class notebook:
    # Notebook
    lnkNotebook_name = "Notebook"
    lnkMoreItems_xpath = "//*[@id='root']/div/div[2]/div[1]/div/div[8]/div/button"

    drpOpenSyllabus_xpath = "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[4]/form/div[1]/div[1]/div/div/div"
    drpSelectSyllsbus_xpath = "//div[@id='menu-syllabus_id']/div[3]/ul/li[10]"

    drpOpenClass_xpath = "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[4]/form/div[1]/div[2]/div/div/div"
    drpSelectClass_xpah = "//div[@id='menu-class_id']/div[3]/ul/li[2]"

    drpOpenSubject_xpath = "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[4]/form/div[1]/div[3]/div/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-subject_id']/div[3]/ul/li[3]"

    drpOpenTutor_xpath = "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[4]/form/div[1]/div[4]/div/div/div"
    drpSelectTutor_xpath = "//div[@id='menu-tutor_id']/div[3]/ul/li[2]"

    txtAreaDescription_xpath = "//div[@id='root']/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/form/div[2]/div[2]/div"

    btnSubmit_xpath = "//div[@id='root']/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/form/div[3]/div/div/button/span"
    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div[2]/div[2]/input"

    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div[2]/div[2]/button"
    btnDelete_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/button[2]"
    btnConfirmDelete_xpath = "/html/body/div[2]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMoreItems(self):
        self.driver.find_element(By.XPATH, self.lnkMoreItems_xpath).click()

    def clickOnNotebookMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkNotebook_name).click()

    def drpSyllabus(self):
        self.driver.find_element(By.XPATH, self.drpOpenSyllabus_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSyllsbus_xpath).click()

    def drpClass(self):
        self.driver.find_element(By.XPATH, self.drpOpenClass_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectClass_xpah).click()

    def drpSubject(self):
        self.driver.find_element(By.XPATH, self.drpOpenSubject_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSubject_xpath).click()

    def drpTutor(self):
        self.driver.find_element(By.XPATH, self.drpOpenTutor_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectTutor_xpath).click()

    def setDescription(self, notebook):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(notebook)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchNotebook(self, notebook):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(notebook)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def clickOnDelete(self):
        self.driver.find_element(By.XPATH, self.btnDelete_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btnConfirmDelete_xpath).click()
