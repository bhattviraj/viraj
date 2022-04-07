from selenium.webdriver.common.by import By


class ClassData:
    # ClassData
    lnkText_Classes_name = "Classes"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/button"

    drpOpenSyllabus_xpath = "/html/body/div[4]/div/div/div[2]/form/div[1]/div[1]/div/div"
    drpSelectSyllabus_xpath = "//div[@id='menu-syllabus_dropdown']/div[3]/ul/li[7]"

    txtClassName_xpath = "/html/body/div[4]/div/div/div[2]/form/div[1]/div[2]/div/div/input"

    drpOpenLevel_xpath = "/html/body/div[4]/div/div/div[2]/form/div[2]/div/div/div"
    drpSelectLevel_xpath = "//div[@id='menu-level_id']/div[3]/ul/li[3]"

    # btnResourceType_xpath = "(//input[@name='type'])[2]"

    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"
    btnSubmit_xpath = "/html/body/div[4]/div/div/div[2]/form/div[5]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/input"
    txtSearchClassData_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/div/input"
    txtSearchCreatedDate_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/div/div/input"
    txtSearchStatus_xpath = "NA"

    btnClickOnDelete_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[2]/td[9]/div/button[3]"
    btnClickOnConfirmDelete_xpath = "/html/body/div[4]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnClassDataMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkText_Classes_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def drpSyllabus(self):
        self.driver.find_element(By.XPATH, self.drpOpenSyllabus_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSyllabus_xpath).click()

    def setClassDataName(self, classdata):
        self.driver.find_element(By.XPATH, self.txtClassName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtClassName_xpath).send_keys(classdata)

    def drpLevel(self):
        self.driver.find_element(By.XPATH, self.drpOpenLevel_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectLevel_xpath).click()

    def setDescription(self, classdata):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(classdata)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchClassData(self, classdata):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(classdata)

    def setSearchClassDataName(self, classdata):
        self.driver.find_element(By.XPATH, self.txtSearchClassData_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchClassData_xpath).send_keys(classdata)

    def setSearchClassDataCreatedDate(self, classdata):
        self.driver.find_element(By.XPATH, self.txtSearchCreatedDate_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchCreatedDate_xpath).send_keys(classdata)

    def clickOnDelete(self):
        self.driver.find_element(By.XPATH, self.btnClickOnDelete_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClickOnConfirmDelete_xpath).click()
