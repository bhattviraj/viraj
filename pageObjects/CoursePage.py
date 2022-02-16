class course:
    # Course

    lnkMoreItems_xpath = "//*[@id='root']/div/div[2]/div[1]/div/div[8]/div/button"
    lnkCourse_name = "Course"

    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/button"

    txtTitle_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/input"

    radiobtnType = "(//input[@name='type'])[2]"

    drpOpenSyllabus_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div"
    drpSelectSyllsbus_xpath = "//div[@id='menu-syllabus_id']/div[3]/ul/li[10]"

    drpOpenClass_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div"
    drpSelectClass_xpah = "//div[@id='menu-class_id']/div[3]/ul/li[3]"

    drpOpenSubject_xpath = "/html/body/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div"
    drpSelectSubject_xpath = "//div[@id='menu-subject_id']/div[3]/ul/li[4]"

    drpOpenMode_xpath = "/html/body/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div"
    drpSelectMode_xpath = "//div[@id='menu-mode_of_teaching']/div[3]/ul/li[3]"

    txtCost_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/input"

    txtStartDate_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[2]/div/div/input"
    txtEndDate_xpath = "/html/body/div[2]/div/div/div[2]/form/div[5]/div[1]/div/div/input"

    uploadSampleImage_xpath = "/html/body/div[2]/div/div/div[2]/form/div[6]/div[2]/div/div/input"
    uploadDemoVideo_xpath = "/html/body/div[2]/div/div/div[2]/form/div[7]/div[1]/div/div/input"
    uploadLogo_xpath = "/html/body/div[2]/div/div/div[2]/form/div[7]/div[2]/div/div/input"

    txtNumberOfVideos_xpath = "/html/body/div[2]/div/div/div[2]/form/div[8]/div[1]/div/div/input"
    txtNumberOfAssignements = "/html/body/div[2]/div/div/div[2]/form/div[8]/div[2]/div/div/input"

    txtCourseTopics_xpath = "/html/body/div[2]/div/div/div[2]/form/div[9]/div[2]/div/div/input"

    radiobtnCourseType = "//input[@name='course_type']"

    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"

    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[13]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMoreItems(self):
        self.driver.find_element_by_xpath(self.lnkMoreItems_xpath).click()

    def clickOnCourseMenu(self):
        self.driver.find_element_by_link_text(self.lnkCourse_name).click()

    def clickOnAdd(self):
        self.driver.find_element_by_xpath(self.btnAdd_xpath).click()

    def setTitle(self, textbook):
        self.driver.find_element_by_xpath(self.txtTitle_xpath).clear()
        self.driver.find_element_by_xpath(self.txtTitle_xpath).send_keys(textbook)

    def selectTechType(self):
        self.driver.find_element_by_xpath(self.radiobtnType).click()

    def drpSyllabus(self):
        self.driver.find_element_by_xpath(self.drpOpenSyllabus_xpath).click()
        self.driver.find_element_by_xpath(self.drpSelectSyllsbus_xpath).click()

    def drpClass(self):
        self.driver.find_element_by_xpath(self.drpOpenClass_xpath).click()
        self.driver.find_element_by_xpath(self.drpSelectClass_xpah).click()

    def drpSubject(self):
        self.driver.find_element_by_xpath(self.drpOpenSubject_xpath).click()
        self.driver.find_element_by_xpath(self.drpSelectSubject_xpath).click()

    def drpMode(self):
        self.driver.find_element_by_xpath(self.drpOpenMode_xpath).click()
        self.driver.find_element_by_xpath(self.drpSelectMode_xpath).click()

    def setCost(self, course):
        self.driver.find_element_by_xpath(self.txtCost_xpath).clear()
        self.driver.find_element_by_xpath(self.txtCost_xpath).send_keys(course)

    def setStartDate(self, course):
        self.driver.find_element_by_xpath(self.txtStartDate_xpath).clear()
        self.driver.find_element_by_xpath(self.txtStartDate_xpath).send_keys(course)

    def setEndDate(self, course):
        self.driver.find_element_by_xpath(self.txtEndDate_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEndDate_xpath).send_keys(course)

    def setSmapleImage(self, course):
        self.driver.find_element_by_xpath(self.uploadSampleImage_xpath).clear()
        self.driver.find_element_by_xpath(self.uploadSampleImage_xpath).send_keys(course)

    def setDemoVideo(self, course):
        self.driver.find_element_by_xpath(self.uploadDemoVideo_xpath).clear()
        self.driver.find_element_by_xpath(self.uploadDemoVideo_xpath).send_keys(course)

    def setLogo(self, course):
        self.driver.find_element_by_xpath(self.uploadLogo_xpath).clear()
        self.driver.find_element_by_xpath(self.uploadLogo_xpath).send_keys(course)

    def setNumberOfVideos(self, course):
        self.driver.find_element_by_xpath(self.txtNumberOfVideos_xpath).clear()
        self.driver.find_element_by_xpath(self.txtNumberOfVideos_xpath).send_keys(course)

    def setNumberOfAssignements(self, course):
        self.driver.find_element_by_xpath(self.txtNumberOfAssignements).clear()
        self.driver.find_element_by_xpath(self.txtNumberOfAssignements).send_keys(course)

    def setCourseTopics(self, course):
        self.driver.find_element_by_xpath(self.txtCourseTopics_xpath).clear()
        self.driver.find_element_by_xpath(self.txtCourseTopics_xpath).send_keys(course)

    def selectCourseType(self):
        self.driver.find_element_by_xpath(self.radiobtnCourseType).click()

    def setDescription(self, course):
        self.driver.find_element_by_xpath(self.txtAreaDescription_xpath).clear()
        self.driver.find_element_by_xpath(self.txtAreaDescription_xpath).send_keys(course)

    def clickOnSubmit(self):
        self.driver.find_element_by_xpath(self.btnSubmit_xpath).click()

    def setSearchCourse(self, tuition):
        self.driver.find_element_by_xpath(self.txtSearch_xpath).clear()
        self.driver.find_element_by_xpath(self.txtSearch_xpath).send_keys(tuition)

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()
