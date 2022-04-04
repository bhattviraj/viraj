import time
import unittest

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.EventPage import Event
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string


class Test_010_event:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_event(self, setup):
        self.logger.info("************* Test_010_event **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add event Test **********")
        self.event = Event(self.driver)
        time.sleep(3)
        self.event.clickOnMoreItems()
        time.sleep(2)
        self.event.clickOnEventsMenu()  # Click on Menu Item
        time.sleep(4)
        self.event.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access Add event page
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                # change the control to Add event page
                self.driver.switch_to.window(login_page)
                self.logger.info("************* Providing event info **********")

        self.event.setTitle("Summer Event")
        self.event.setTopic("Computer")
        self.event.setDescription("Summer Event Demo 2022")
        self.event.drpTargetAudience()
        self.event.drpMode()
        self.event.setPrice("111")
        self.event.setEventImage("D:/Documents/Downloads/network.jpg")

        # self.event.setStartDate("13/01/2022")

        # self.event.setEndDate("30/01/2022")

        self.event.clickOnAddEvent()
        time.sleep(5)

        self.logger.info("************* Saving event info **********")

        self.logger.info("********* Add event validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'Event added successfully.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  event Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add event test **********")

    def test_searchEvent(self, setup):
        self.logger.info("************* Test_010_search event **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.event = Event(self.driver)
        time.sleep(3)
        self.event.clickOnMoreItems()
        time.sleep(3)
        self.event.clickOnEventsMenu() # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search event**********")

        self.event.setSearchEvent("Demo")
        time.sleep(3)
        self.event.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search event validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "Demo" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        elif "Events data not available..." in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchEvent_scr.png")  # Screenshot
            self.logger.error("********* Search event Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")
