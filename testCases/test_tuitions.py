import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.TuitionPage import Tuitions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_010_tuitions:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    def test_tuitions(self, setup):
        self.logger.info("************* Test_010_tuitions **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Tuitions Test **********")
        self.tuitions = Tuitions(self.driver)
        time.sleep(3)
        self.tuitions.clickOnTuitionsMenu()  # Click on Menu Item
        time.sleep(4)
        self.tuitions.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access Add tuition page
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                # change the control to Add Tuition page
                self.driver.switch_to.window(login_page)
                self.logger.info("************* Providing Tuitions info **********")

        self.tuitions.setTitle("Tuition Class")
        self.tuitions.selectType()
        self.tuitions.drpSyllabus()
        time.sleep(3)
        self.tuitions.drpClass()
        time.sleep(3)
        self.tuitions.drpSubject()
        time.sleep(2)
        self.tuitions.drpMode()
        self.tuitions.setCost("1111")

        #self.tuitions.setStartDate("13/01/2022")

        #self.tuitions.setEndDate("30/01/2022")
        time.sleep(5)
        self.tuitions.setTuitionImage("D:/Documents/Downloads/network.jpg")
        time.sleep(5)
        self.tuitions.setDescription("Test Tuition")
        self.tuitions.CheckSchedule()
        time.sleep(6)
        self.tuitions.clickOnSubmit()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/button").click()
        time.sleep(5)

        self.logger.info("************* Saving Tuition info **********")

        self.logger.info("********* Add Tuition validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'Job Posted Successfully.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Tuitions Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Tuition test **********")

    def test_searchTuition(self,setup):
        self.logger.info("************* Test_010_search Tuition **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.tuitions = Tuitions(self.driver)
        time.sleep(5)
        self.tuitions.clickOnTuitionsMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search tuition**********")

        searched_value = self.tuitions.setSearchTuition("Literature:")
        time.sleep(3)
        self.tuitions.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search tuition validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Literature:" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Tuition Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")