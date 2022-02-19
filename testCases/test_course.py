import unittest

import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.CoursePage import course
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_014_course:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_course(self, setup):
        self.logger.info("************* Test_014_course **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add course Test **********")
        self.course = course(self.driver)
        time.sleep(3)
        self.course.clickOnMoreItems()
        time.sleep(2)
        self.course.clickOnCourseMenu()  # Click on Menu Item
        time.sleep(4)
        self.course.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access Add course page
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                # change the control to Add course page
                self.driver.switch_to.window(login_page)
                self.logger.info("************* Providing course info **********")

        self.course.setTitle("course Class")
        self.course.selectTechType()
        self.course.drpSyllabus()
        time.sleep(3)
        self.course.drpClass()
        time.sleep(3)
        self.course.drpSubject()
        time.sleep(2)
        self.course.drpMode()
        self.course.setCost("1111")

        # self.course.setStartDate("13/01/2022")

        # self.course.setEndDate("30/01/2022")
        time.sleep(5)
        self.course.setSmapleImage("D:/Documents/Downloads/network.jpg")
        time.sleep(5)
        self.course.setDemoVideo("D:/Documents/Downloads/demo1.mp4")
        self.course.setLogo("D:/Documents/Downloads/network.jpg")
        self.course.setNumberOfVideos("1")
        self.course.setNumberOfAssignements("1")
        self.course.setCourseTopics("1")
        self.course.selectCourseType()
        self.course.setDescription("Test course")
        time.sleep(4)
        self.course.clickOnSubmit()
        time.sleep(6)
        self.logger.info("************* Saving course info **********")

        self.logger.info("********* Add course validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        exp_alert = "Course created successfully."
        # act_alert = self.driver.find_element_by_xpath("//div[2]")
        if 'Course created successfully.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  course Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add course Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add course test **********")

    @pytest.mark.sanity
    def test_searchcourse(self, setup):
        self.logger.info("************* Test_010_search course **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.course = course(self.driver)
        time.sleep(5)
        self.course.clickOnMoreItems()
        time.sleep(2)
        self.course.clickOnCourseMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search course**********")

        searched_value = self.course.setSearchCourse("Demo")
        time.sleep(3)
        self.course.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search course validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Demo" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        elif "Course data not available..." in self.msg:
            assert True
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search course Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_Deletecourse(self, setup):
        self.logger.info("************* Test_018_course **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Delete course Test **********")
        self.course = course(self.driver)
        time.sleep(5)
        self.course.clickOnMoreItems()
        time.sleep(2)
        self.course.clickOnCourseMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("*************Delete course**********")

        self.course.clickOnAllCoursesOption()
        time.sleep(3)
        self.course.clickOnDeleteCourse()
        time.sleep(3)
        self.logger.info("*************Delete course **********")

        self.logger.info("*********Delete course validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Course deleted from database." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Searchcourse_scr.png")  # Screenshot
            self.logger.error("*********Delete My Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")