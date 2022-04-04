import time
from telnetlib import EC

from selenium.webdriver.common.by import By


class TextBook:
    # TexBook
    lnkText_book_name = "Textbook"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div/button"

    drpOpenSyllabus_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div"
    drpSelectSyllsbus_xpath = "//div[@id='menu-syllabus_id']/div[3]/ul/li[4]"

    drpOpenClass_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div"
    drpSelectClass_xpah = "//div[@id='menu-class_id']/div[3]/ul/li[2]"

    drpOpenSubject_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-subject_id']/div[3]/ul/li[2]"

    txtBookName_xpath="/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/input"
    txtExternalLink_xpath="/html/body/div[2]/div/div/div[2]/form/div[3]/div[3]/div/div/input"
    uploadBookImage_xpath="/html/body/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div/input"
    #btnResourceType_xpath = "(//input[@name='type'])[2]"

    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"
    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[5]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/button"

    btnClickonOption_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/li/a/img"
    btnClickonDelete_xpath = "//a[contains(text(),'Delete')]"
    btnClickOnConfirnDelete_xpath = "/html/body/div[2]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTextBookMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkText_book_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def drpSyllabus(self):
        self.driver.find_element(By.XPATH, self.drpOpenSyllabus_xpath).click()
        #self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='menu-syllabus_id']/div[3]/ul/li[10]"))))
        self.driver.find_element(By.XPATH, self.drpSelectSyllsbus_xpath).click()

    def drpClass(self):
        self.driver.find_element(By.XPATH, self.drpOpenClass_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectClass_xpah).click()

    def drpSubject(self):
        self.driver.find_element(By.XPATH, self.drpOpenSubject_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSubject_xpath).click()

    def setBookName(self, textbook):
        self.driver.find_element(By.XPATH, self.txtBookName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBookName_xpath).send_keys(textbook)

    def setBookImage(self, textbook):
        self.driver.find_element(By.XPATH, self.uploadBookImage_xpath).clear()
        self.driver.find_element(By.XPATH, self.uploadBookImage_xpath).send_keys(textbook)

    def setExternalLink(self, textbook):
        self.driver.find_element(By.XPATH, self.txtExternalLink_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtExternalLink_xpath).send_keys(textbook)

    def setDescription(self, textbook):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(textbook)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchTextBook(self, textbook):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(textbook)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def clickOnOption(self):
        self.driver.find_element(By.XPATH, self.btnClickonOption_xpath).click()

    def clickOnDelete(self):
        self.driver.find_element(By.XPATH, self.btnClickonDelete_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClickOnConfirnDelete_xpath).click()
