import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddPostJob import AddPostJob
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_0008_postJob:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    def test_postJob(self, setup):
        self.logger.info("************* Test_008_PostJob **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Post Job Test **********")
        self.postjob = AddPostJob(self.driver)
        time.sleep(3)
        self.postjob.clickOnPostSearchJobMenu()  # Click on Menu Item
        time.sleep(4)
        self.postjob.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                # change the control to signin page
                self.driver.switch_to.window(login_page)
                self.logger.info("************* Providing Post Job info **********")

        self.postjob.drpSyllabus()
        time.sleep(3)
        self.postjob.drpClass()
        time.sleep(3)
        self.postjob.drpSubject()
        time.sleep(2)
        self.postjob.drpMode()
        self.postjob.radioTeachType()
        self.postjob.setTopic("Hindi Basic")
        #self.postjob.setStarTime("09:00 am")

        #self.postjob.setEndTime("10:00 am")

        self.postjob.setRequirements("Test requirements")
        self.postjob.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving Post Job info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'Job Posted Successfully.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Post Job Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Post Job test **********")

    def test_searchJob(self,setup):
        self.logger.info("************* Test_008_search Job **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.postjob = AddPostJob(self.driver)
        time.sleep(5)
        self.postjob.clickOnPostSearchJobMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search Post Job**********")

        searched_value = self.postjob.setSearchJob("viraj")

        self.postjob.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search Post job validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Literature" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")