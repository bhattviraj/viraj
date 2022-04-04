import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.MySessionPage import mysessions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_013_session:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_search_session(self,setup):
        self.logger.info("************* Test_013_search session **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search  session Test **********")
        self.session = mysessions(self.driver)
        time.sleep(5)

        self.session.clickMysessionMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search  session **********")

        searched_value = self.session.setSearchSession("Literature: ")
        time.sleep(3)
        self.session.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching  session **********")

        self.logger.info("********* Search  session started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Upcoming sessions data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search  session Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")