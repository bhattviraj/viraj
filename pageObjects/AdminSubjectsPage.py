from selenium.webdriver.common.by import By

class Subjects:
    # Subjects
    lnkText_Subjects_name = "Subjects"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/button"

    drpOpenSubject_xpath = "/html/body/div[4]/div/div/div[2]/form/div[1]/div[1]/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-class_id']/div[3]/ul/li[10]"

    txtSubjectName_xpath = "/html/body/div[4]/div/div/div[2]/form/div[1]/div[2]/div/div/input"

    drpOpenLevel_xpath = "/html/body/div[4]/div/div/div[2]/form/div[2]/div/div/div"
    drpSelectLevel_xpath = "//div[@id='menu-level_id']/div[3]/ul/li[3]"

    # btnResourceType_xpath = "(//input[@name='type'])[2]"

    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"
    btnSubmit_xpath = "/html/body/div[4]/div/div/div[2]/form/div[4]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/input"
    txtSearchSubjects_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/div/input"
    txtSearchCreatedDate_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[4]/div/div/input"
    txtSearchStatus_xpath = "NA"

    btnClickOnDelete_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[7]/div/button[3]"
    btnClickOnConfirmDelete_xpath = "/html/body/div[4]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSubjectsMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkText_Subjects_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def drpSubject(self):
        self.driver.find_element(By.XPATH, self.drpOpenSubject_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectSubject_xpath).click()

    def setSubjectsName(self, subjects):
        self.driver.find_element(By.XPATH, self.txtSubjectName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSubjectName_xpath).send_keys(subjects)

    def setDescription(self, subjects):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(subjects)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchSubjects(self, subjects):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(subjects)

    def setSearchSubjectsName(self, subjects):
        self.driver.find_element(By.XPATH, self.txtSearchSubjects_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchSubjects_xpath).send_keys(subjects)

    def setSearchSubjectsCreatedDate(self, subjects):
        self.driver.find_element(By.XPATH, self.txtSearchCreatedDate_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchCreatedDate_xpath).send_keys(subjects)

    def clickOnDelete(self):
        self.driver.find_element(By.XPATH, self.btnClickOnDelete_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClickOnConfirmDelete_xpath).click()
