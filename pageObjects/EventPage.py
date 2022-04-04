from selenium.webdriver.common.by import By


class Event:
    # Event
    lnkMoreItems_xpath = "//*[@id='root']/div/div[2]/div[1]/div/div[8]/div/button"
    lnkEvent_name = "Events"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div/button"

    txtTitle_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div/input"
    txtTopic_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/input"

    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"

    drpOpenTargetAudience_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div"
    drpSelectTargetAudience_xpath = "//div[@id='menu-target_audience']/div[3]/ul/li[4]"

    drpOpenMode_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[2]/div/div"
    drpSelectMode_xpath = "//div[@id='menu-mode']/div[3]/ul/li[2]"

    txtPrice_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[3]/div/div/input"

    uploadEventImage_xpath = "/html/body/div[2]/div/div/div[2]/form/div[4]/div[4]/div/div/input"

    txtStartDate_xpath = "/html/body/div[2]/div/div/div[2]/form/div[8]/div[1]/div/div/input"
    txtEndDate_xpath = "/html/body/div[2]/div/div/div[2]/form/div[8]/div[2]/div/div/input"

    txtStartTime_xpath = "/html/body/div[2]/div/div/div[2]/form/div[9]/div[1]/div/div/input"
    txtEndTime_xpath = "/html/body/div[2]/div/div/div[2]/form/div[9]/div[2]/div/div/input"

    btnAddEvent_xpath = "/html/body/div[2]/div/div/div[2]/form/div[10]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMoreItems(self):
        self.driver.find_element(By.XPATH, self.lnkMoreItems_xpath).click()

    def clickOnEventsMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkEvent_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def setTitle(self, event):
        self.driver.find_element(By.XPATH, self.txtTitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtTitle_xpath).send_keys(event)

    def setTopic(self, event):
        self.driver.find_element(By.XPATH, self.txtTopic_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtTopic_xpath).send_keys(event)

    def setDescription(self, event):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(event)

    def drpTargetAudience(self):
        self.driver.find_element(By.XPATH, self.drpOpenTargetAudience_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectTargetAudience_xpath).click()

    def drpMode(self):
        self.driver.find_element(By.XPATH, self.drpOpenMode_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectMode_xpath).click()

    def setPrice(self, event):
        self.driver.find_element(By.XPATH, self.txtPrice_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPrice_xpath).send_keys(event)

    def setEventImage(self, event):
        self.driver.find_element(By.XPATH, self.uploadEventImage_xpath).clear()
        self.driver.find_element(By.XPATH, self.uploadEventImage_xpath).send_keys(event)

    def setStartDate(self, event):
        self.driver.find_element(By.XPATH, self.txtStartDate_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtStartDate_xpath).send_keys(event)

    def setEndDate(self, event):
        self.driver.find_element(By.XPATH, self.txtEndDate_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEndDate_xpath).send_keys(event)

    def setStartTime(self, event):
        self.driver.find_element(By.XPATH, self.txtStartTime_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtStartTime_xpath).send_keys(event)

    def setEndTime(self, event):
        self.driver.find_element(By.XPATH, self.txtEndTime_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEndTime_xpath).send_keys(event)

    def clickOnAddEvent(self):
        self.driver.find_element(By.XPATH, self.btnAddEvent_xpath).click()

    def setSearchEvent(self, event):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(event)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()