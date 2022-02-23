from selenium.webdriver.common.by import By

class AddPostJob:
    # Add TodoTask
    lnkPost_search_job_name = "Post & Search Job"
    btnAdd_xpath = "//div[@id='root']/div/div[2]/div[2]/div/div/div/div/div/div/div/div/button"

    drpOpenSyllabus_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div"
    drpSelectSyllsbus_xpath = "//*[contains(text(), 'CBSE')]"

    drpOpenClass_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div"
    drpSelectClass_xpah = "//*[contains(text(), '10th')]"

    drpOpenSubject_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-subject_id']/div[3]/ul/li[4]"

    drpOpenMode_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/div"
    drpSelectMode_xpath = "//div[@id='menu-mode']/div[3]/ul/li[3]"

    btnTeachTypeRadio_xpath = "(//input[@name='type'])[2]"

    txtTopic_xpath = "//input[@name='topic']"

    txtStartTime_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/input"
    txtEndTime_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[2]/div/div/input"
    txtAreaRequirements_xpath = "//textarea[@id='outlined-multiline-static']"
    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[6]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnPostSearchJobMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkPost_search_job_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

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

    def drpMode(self):
        self.driver.find_element(By.XPATH, self.drpOpenMode_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectMode_xpath).click()

    def radioTeachType(self):
        self.driver.find_element(By.XPATH, self.btnTeachTypeRadio_xpath).click()

    def setTopic(self, addpost):
        self.driver.find_element(By.XPATH, self.txtTopic_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtTopic_xpath).send_keys(addpost)

    def setStarTime(self, addpost):
        self.driver.find_element(By.XPATH, self.txtStartTime_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtStartTime_xpath).send_keys(addpost)

    def setEndTime(self, addpost):
        self.driver.find_element(By.XPATH, self.txtEndTime_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEndTime_xpath).send_keys(addpost)

    def setRequirements(self, addpost):
        self.driver.find_element(By.XPATH, self.txtAreaRequirements_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaRequirements_xpath).send_keys(addpost)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchJob(self, addpost):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(addpost)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
