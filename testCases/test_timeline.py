import unittest

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.timelinePage import Timeline
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_0018_Timeline:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_AddTimeline(self, setup):
        self.logger.info("************* Test_008_PostJob **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting timeline Test **********")
        self.timeline = Timeline(self.driver)
        time.sleep(3)
        self.timeline.clickOnTimelineMenu() # Click on Menu Item
        time.sleep(8)
        self.timeline.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                # change the control to page
                self.driver.switch_to.window(login_page)
                self.logger.info("************* Providing Timeline info **********")

        self.timeline.drpTargetAudience()
        time.sleep(3)
        self.timeline.setDescription("Demo Timeline")
        self.timeline.setTimelineImage("D:/Documents/Downloads/network.jpg")
        #self.timeline.setTimelineVideo("D:/Documents/Downloads/network.jpg")
        self.timeline.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving Post Job info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'Timeline posted successfully.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Post Job Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending timeline test **********")

    @unittest.skip
    def test_searchTimeline(self,setup):
        self.logger.info("************* Test_018_timeline **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.timeline = Timeline(self.driver)
        time.sleep(5)
        self.timeline.clickOnTimelineMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search Post Job**********")

        searched_value = self.timeline.setSearchTimeline("viraj")

        self.timeline.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Timeline **********")

        self.logger.info("********* Search Timeline validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Viraj" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchTimeline_scr.png")  # Screenshot
            self.logger.error("********* Search Timeline Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_timelineRepost(self,setup):
        self.logger.info("************* Test_018_timeline **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Repost Timeline Test **********")
        self.timeline = Timeline(self.driver)
        time.sleep(5)
        self.timeline.clickOnTimelineMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Repost Timeline**********")
        if "TimeLine data not available..." in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
            self.driver.close()
        else:
            self.timeline.clickOnoption()
            time.sleep(2)
            self.timeline.clickOnTimelineRepost()
            time.sleep(3)
            self.logger.info("************* Repost Timeline **********")

            self.logger.info("********* Repost Timeline validation started *****************")



            if "Timeline posted successfully." in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Test Passed *********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchTimeline_scr.png")  # Screenshot
                self.logger.error("********* Search Timeline Test Failed ************")
                assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_DeleteMyTimeline(self,setup):
        self.logger.info("************* Test_018_timeline **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Delete My Timeline Test **********")
        self.timeline = Timeline(self.driver)
        time.sleep(5)
        self.timeline.clickOnTimelineMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("*************Delete My Timeline**********")

        self.timeline.clickOnMyTimeline()
        time.sleep(3)
        self.timeline.clickOnMytimelineOption()
        time.sleep(3)
        self.timeline.clickOnDeleteMytimeline()
        time.sleep(3)
        self.logger.info("*************Delete My Timeline **********")

        self.logger.info("*********Delete My validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Timeline deleted from successfully." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchTimeline_scr.png")  # Screenshot
            self.logger.error("*********Delete Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")