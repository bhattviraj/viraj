import time

from selenium.webdriver.common.by import By


class Timeline:
    # Add Timeline
    lnkTimeline_name = "Timeline"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/button"

    drpOpenTargetAudience_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div"
    drpSelectTragerAudience_xpath = "//div[3]/ul/li[4]"

    fileTimelineImage_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div/div/input"
    fileTimelineVideo_xpath = "/html/body/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/input"
    txtAreaDescription_xpath = "//*[@id='outlined-multiline-static']"
    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/button"

    lsOption_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[3]/div/div/li"
    lsTimelineRepost_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[3]/div/div/li/ul/li[2]/a"
    btnConfirmRepost_xpath = "/html/body/div[2]/div/div[3]/button[1]"

    btnMyTimeline_xpath = "//*[@id='MyTimeline']"
    lsMytimelineOption_xpath= "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[3]/div/div/li"
    lsDeleteMyTimeline_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[3]/div/div/li/ul/li[2]"
    btnConfirmDeleteMyTimeline_xpath = "/html/body/div[2]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTimelineMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkTimeline_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def drpTargetAudience(self):
        self.driver.find_element(By.XPATH, self.drpOpenTargetAudience_xpath).click()
        self.driver.find_element(By.XPATH, self.drpSelectTragerAudience_xpath).click()

    def setDescription(self, timeline):
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAreaDescription_xpath).send_keys(timeline)

    def setTimelineImage(self, timeline):
        self.driver.find_element(By.XPATH, self.fileTimelineImage_xpath).clear()
        self.driver.find_element(By.XPATH, self.fileTimelineImage_xpath).send_keys(timeline)

    def setTimelineVideo(self, timeline):
        self.driver.find_element(By.XPATH, self.fileTimelineVideo_xpath).clear()
        self.driver.find_element(By.XPATH, self.fileTimelineVideo_xpath).send_keys(timeline)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchTimeline(self, timeline):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(timeline)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def clickOnoption(self):
        self.driver.find_element(By.XPATH, self.lsOption_xpath).click()

    def clickOnTimelineRepost(self):
        self.driver.find_element(By.XPATH, self.lsTimelineRepost_xpath).click()
        self.driver.find_element(By.XPATH, self.btnConfirmRepost_xpath).click()

    def clickOnMyTimeline(self):
        self.driver.find_element(By.XPATH, self.btnMyTimeline_xpath).click()

    def clickOnMytimelineOption(self):
        self.driver.find_element(By.XPATH, self.lsMytimelineOption_xpath).click()

    def clickOnDeleteMytimeline(self):
        self.driver.find_element(By.XPATH, self.lsDeleteMyTimeline_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btnConfirmDeleteMyTimeline_xpath).click()

