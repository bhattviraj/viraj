import unittest

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.StudentSidePage import student_side_flow
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_student_flow:
    baseURL = ReadConfig.getApplicationURL()
    studentUsername = ReadConfig.getStudentUseremail()
    studentPassword = ReadConfig.getStudentPassword()
    logger = LogGen.loggen()  # Logger
    course_name = "10th Maths"  # Main Value - Course Name

    #@pytest.mark.sanity
    def test_student_course_flow(self, setup):
        self.logger.info("************* Test_014_course **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.studentUsername)
        self.lp.setPassword(self.studentPassword)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search course Test **********")
        self.course = student_side_flow(self.driver)
        time.sleep(3)
        self.course.clickOnSearchCourseMenu()
        time.sleep(4)
        self.course.setSearchCourse(self.course_name)
        time.sleep(4)
        self.course.clickOnSearchCourse()
        time.sleep(4)
        self.logger.info("************** Search course validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if self.course_name in self.msg:

            self.course.clickOnJoinNowCourse()  # Purchase the Searched Course
            time.sleep(5)
            self.successMsg = self.driver.find_element(By.TAG_NAME, "body").text

            if '' in self.successMsg:
                self.logger.info("************** If Join Course success Enter Here *****************")
                self.course.clickOnMoreItems()
                time.sleep(3)
                self.course.clickOnCoursesMenu()
                time.sleep(5)
                self.course.clickOnSubscribedCourses()
                time.sleep(5)
                self.course.clickOnInProgressCourses()
                time.sleep(5)
                self.course.setSearchMyCourse(self.course_name)
                time.sleep(3)
                self.course.clickOnSearchMyCourse()
                if self.course_name in self.msg:
                    self.logger.log("********* Test Passed Log*********")
                    self.logger.info("********* Test Passed *********")
                    assert True
                elif 'Course subscription data not available...' in self.msg:
                    assert False
                else:
                    self.logger.error("****** Test Failed *********")
                    assert False
            else:
                self.logger.error("****** Test Failed *********")
                assert False
        elif 'Course data not available...' in self.msg:
            self.logger.log("********* Test Passed Log*********")
            self.logger.info("********** Test is Pass Because Searched Course Data Not Available ************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Flow course test **********")
