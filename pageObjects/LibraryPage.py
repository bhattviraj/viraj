import time
from telnetlib import EC

from selenium.webdriver.common.by import By


class Library:
    # Library
    lnkMoreItems_xpath = "//*[@id='root']/div/div[2]/div[1]/div/div[8]/div/button"
    lnkLibrary_name = "Library"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/button"

    txtTitle_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/input"

    drpOpenSyllabus_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div"
    drpSelectSyllsbus_xpath = "//div[@id='menu-syllabus_id']/div[3]/ul/li[10]"

    drpOpenClass_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div/div"
    drpSelectClass_xpah = "//div[@id='menu-class_id']/div[3]/ul/li[2]"

    drpOpenSubject_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-subject_id']/div[3]/ul/li[4]"

    fileAttachment_xpath = "/html/body/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div/input"
    fileImage_xpath = "/html/body/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div/input"
    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"
    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[5]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"

    btnClickonOption_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/li/a/img"
    btnClickonDelete_xpath = "//a[contains(text(),'Delete')]"
    btnClickOnConfirnDelete_xpath = "/html/body/div[2]/div/div[3]/button[1]"

    # filter
    drpOpenSyllabusSearch = ""
    drpSelectSyllabusSearch = ""
    drpOpenClassSearch = ""
    drpSelectClassSearch = ""
    drpOpenSubjectSearch = ""
    drpSelectSubjectSearch = ""


    def __init__(self, driver):
        self.driver = driver

    def clickOnMoreItems(self):
        self.driver.find_element(By.XPATH, self.lnkMoreItems_xpath).click()

    def clickOnLibraryMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkLibrary_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def setTitle(self, library):
        self.driver.find_element(By.XPATH, self.txtTitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtTitle_xpath).send_keys(library)

    def drpSyllabus(self):
        self.driver.find_element(By.XPATH, self.drpOpenSyllabus_xpath).click()
        # self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='menu-syllabus_id']/div[3]/ul/li[10]"))))
        self.driver.find_element(By.XPATH, self.drpSelectSyllsbus_xpath).click()

    def drpClass(self):
        self.driver.find_element(By.XPATH, self.drpOpenClass_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectClass_xpah).click()

    def drpSubject(self):
        self.driver.find_element(By.XPATH, self.drpOpenSubject_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSubject_xpath).click()

    def setLibraryAttachment(self, library):
        self.driver.find_element(By.XPATH, self.fileAttachment_xpath).clear()
        self.driver.find_element(By.XPATH, self.fileImage_xpath).send_keys(library)

    def setLibraryImage(self, library):
        self.driver.find_element(By.XPATH, self.fileImage_xpath).clear()
        self.driver.find_element(By.XPATH, self.fileImage_xpath).send_keys(library)

    def setDescription(self, library):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(library)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchlibrary(self, library):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(library)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def clickOnOption(self):
        self.driver.find_element(By.XPATH, self.btnClickonOption_xpath).click()

    def clickOnDelete(self):
        self.driver.find_element(By.XPATH, self.btnClickonDelete_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClickOnConfirnDelete_xpath).click()
