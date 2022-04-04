import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchDataPage import Search
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string

class Test_007_searchfeedback:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_searchfeedback(self,setup):
        self.logger.info("************* Test_006_searchfeedback **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search feedback Test **********")
        self.searchfeedback = Search(self.driver)
        time.sleep(5)
        self.searchfeedback.clickOnFeedbackMenu() # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search feedbackpark**********")

        searched_value = self.searchfeedback.setSearchFeedbackBox("My feedback")

        self.searchfeedback.clickFeedbackSearch()
        time.sleep(3)

        self.logger.info("************* Searching feedback **********")

        self.logger.info("********* Search feedbacktor validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "My feedback" in self.msg:
            time.sleep(2)
            self.logger.info("********* Add customer Test Passed *********")
            assert True
        elif "feedback data not available...":

            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search feedbacktor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")