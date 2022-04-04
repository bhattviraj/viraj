class questionanswers:
    # Question Answers
    lnkquestionanswers_name = "Question & Answers"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/p/button"

    drpOpenSyllabus_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div"
    drpSelectSyllsbus_xpath = "//div[@id='menu-syllabus_id']/div[3]/ul/li[4]"

    drpOpenClass_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div"
    drpSelectClass_xpah = "//div[@id='menu-class_id']/div[3]/ul/li[2]"

    drpOpenSubject_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-subject_id']/div[3]/ul/li[2]"

    txtTopic_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/input"

    txtAreaQuestions_xpath = "//textarea[@id='outlined-multiline-static']"

    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnQusAnsMenu(self):
        self.driver.find_element_by_link_text(self.lnkquestionanswers_name).click()

    def clickOnAdd(self):
        self.driver.find_element_by_xpath(self.btnAdd_xpath).click()

    def drpSyllabus(self):
        self.driver.find_element_by_xpath(self.drpOpenSyllabus_xpath).click()
        self.driver.find_element_by_xpath(self.drpSelectSyllsbus_xpath).click()

    def drpClass(self):
        self.driver.find_element_by_xpath(self.drpOpenClass_xpath).click()
        self.driver.find_element_by_xpath(self.drpSelectClass_xpah).click()

    def drpSubject(self):
        self.driver.find_element_by_xpath(self.drpOpenSubject_xpath).click()
        self.driver.find_element_by_xpath(self.drpSelectSubject_xpath).click()

    def setTopic(self, quaans):
        self.driver.find_element_by_xpath(self.txtTopic_xpath).clear()
        self.driver.find_element_by_xpath(self.txtTopic_xpath).send_keys(quaans)

    def setQuestion(self, qusans):
        self.driver.find_element_by_xpath(self.txtAreaQuestions_xpath).clear()
        self.driver.find_element_by_xpath(self.txtAreaQuestions_xpath).send_keys(qusans)

    def clickOnSubmit(self):
        self.driver.find_element_by_xpath(self.btnSubmit_xpath).click()

    def setSearchJob(self, qusans):
        self.driver.find_element_by_xpath(self.txtSearch_xpath).clear()
        self.driver.find_element_by_xpath(self.txtSearch_xpath).send_keys(qusans)

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()
