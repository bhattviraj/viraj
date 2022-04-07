from selenium.webdriver.common.by import By


class Syllabus:
    # Syllabus
    lnkText_book_name = "Syllabus"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/button"

    txtSyllabusName_xpath = "/html/body/div[4]/div/div/div[2]/form/div[1]/div[1]/div/div/input"
    # btnResourceType_xpath = "(//input[@name='type'])[2]"

    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"
    btnSubmit_xpath = "/html/body/div[4]/div/div/div[2]/form/div[3]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/input"
    txtSearchSyllabus_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/div/input"
    txtSearchCreatedDate_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/div/input"
    txtSearchStatus_xpath = "NA"

    btnClickOnDelete_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[5]/div/button[3]"
    btnClickOnConfirmDelete_xpath = "/html/body/div[4]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSyllabusMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkText_book_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def setSyllabusName(self, syllabus):
        self.driver.find_element(By.XPATH, self.txtSyllabusName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSyllabusName_xpath).send_keys(syllabus)

    def setDescription(self, syllabus):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(syllabus)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchSyllabus(self, syllabus):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(syllabus)

    def setSearchSyllabusName(self, syllabus):
        self.driver.find_element(By.XPATH, self.txtSearchSyllabus_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchSyllabus_xpath).send_keys(syllabus)

    def setSearchSyllabusCreatedDate(self, syllabus):
        self.driver.find_element(By.XPATH, self.txtSearchCreatedDate_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchCreatedDate_xpath).send_keys(syllabus)

    def clickOnDelete(self):
        self.driver.find_element(By.XPATH, self.btnClickOnDelete_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClickOnConfirmDelete_xpath).click()
