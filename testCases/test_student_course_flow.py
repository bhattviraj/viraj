import unittest

import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageObjects.FindTutorPage import FindTutor
from pageObjects.LoginPage import LoginPage
from pageObjects.MessagesPage import Messages
from pageObjects.StudentSidePage import student_side_flow
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


#@pytest.mark.sanity
class Test_student_flow:
    baseURL = ReadConfig.getApplicationURL()
    studentUsername = ReadConfig.getStudentUseremail()
    studentPassword = ReadConfig.getStudentPassword()
    tutorUsername = ReadConfig.getUseremail()
    tutorPassword = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger
    course_name = "CBSE 1Th Math Course"  # Main Value - Course Name
    tutor_name = "Vijay"

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
                    self.logger.info("********* Test Passed *********")
                    assert True
                elif 'Course subscription data not available...' in self.msg:
                    allure.attach(self.driver.get_screenshot_as_png(), name="TestStudentFlowWhenDataNotFound",
                                  attachment_type=AttachmentType.PNG)
                    assert False
                else:
                    self.logger.error("****** Test Failed *********")
                    allure.attach(self.driver.get_screenshot_as_png(), name="TestStudentFlowTutorSomethingWrong",
                                  attachment_type=AttachmentType.PNG)
                    assert False
            else:
                self.logger.error("****** Test Failed *********")
                allure.attach(self.driver.get_screenshot_as_png(), name="TestStudentFlowWhenCoruseNotJoin",
                              attachment_type=AttachmentType.PNG)
                assert False
        elif 'Course data not available...' in self.msg:
            self.logger.info("********** Test is Pass Because Searched Course Data Not Available ************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            allure.attach(self.driver.get_screenshot_as_png(), name="TestStudentFlowSometingWrong",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("********* Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Flow course test **********")
    @unittest.skip
    def test_findtutor(self, setup):
        self.logger.info("************* Test_006_FindTutor **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.studentUsername)
        self.lp.setPassword(self.studentPassword)
        self.lp.clickLogin()
        time.sleep(3)
        #self.lp.verifyLoggedin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutorpark**********")

        searched_value = self.findtutor.setSearchbox(self.tutor_name)

        self.findtutor.clickSearch()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if self.tutor_name in self.msg:

            self.findtutor.openMsgPopUp()
            time.sleep(3)
            self.findtutor.setMessage("Hello Sir/Mam i Want to join your course")
            time.sleep(2)
            self.findtutor.clickOnSendMessage()
            time.sleep(4)
            successMsg = self.driver.find_element(By.XPATH,
                                                        "/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div[2]").text
            if successMsg == "Message Sent Successfully.":
                self.logger.info("********* Test Passed Message Send Successful *********")
                self.lp.clickLogout() #Logout As a Student
                time.sleep(3)
                self.driver.get(self.baseURL)
                time.sleep(3)
                self.lp.setUserName(self.tutorUsername)
                self.lp.setPassword(self.tutorPassword)
                self.lp.clickLogin()
                #self.lp.verifyLoggedin()
                self.logger.info("************* Login successful **********")
                self.logger.info("******* Starting Message Test **********")
                self.messages = Messages(self.driver)
                time.sleep(5)
                self.messages.clickOnMessagaesMenu()  # Click on Menu Item
                time.sleep(4)
                self.messages.setSearch("viraj")
                self.messages.clickOnSearch()
                self.messages.clickOnUserChat()
                self.messages.setMessage("Hello")
                self.messages.clickOnSendMessage()

                #assert True
            else:
                self.logger.info("********* Test Failed Message not Send *************")
                allure.attach(self.driver.get_screenshot_as_png(), name="TestStudentFlowTutorMsg",
                              attachment_type=AttachmentType.PNG)
                assert False
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            allure.attach(self.driver.get_screenshot_as_png(), name="TestStudentFlowFindTutor",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Search Tutor test **********")