import unittest

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.QuestionAnswersPage import questionanswers
from pageObjects.SearchDataPage import Search
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_012_Question_Answers:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_QuestionAnswers(self, setup):
        self.logger.info("************* Test_008_QuestionAnswers **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Question & Answers Test **********")
        self.QuestionAnswers = questionanswers(self.driver)
        time.sleep(3)
        self.QuestionAnswers.clickOnQusAnsMenu()  # Click on Menu Item
        time.sleep(4)
        self.QuestionAnswers.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                # change the control to signin page
                self.driver.switch_to.window(login_page)
                self.logger.info("************* Providing Question & Answers info **********")

        self.QuestionAnswers.drpSyllabus()
        time.sleep(3)
        self.QuestionAnswers.drpClass()
        time.sleep(3)
        self.QuestionAnswers.drpSubject()
        time.sleep(2)
        self.QuestionAnswers.setTopic("Hindi Basic")

        self.QuestionAnswers.setQuestion("Test requirements")
        self.QuestionAnswers.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving Question & Answers info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'Question added successfully.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Question & Answers Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Question & Answers test **********")

    def test_search_QuestionAnswers_with_syllabus(self, setup):

        self.logger.info("************* Test_09_Search Text Book With Syllabus **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Text Book Test **********")
        self.searchQuestionAnswers = Search(self.driver)
        time.sleep(5)
        self.searchQuestionAnswers.clickOnQuestionAnswersMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Text Book **********")

        self.searchQuestionAnswers.drpSyllabus("CBSE")
        time.sleep(3)
        self.searchQuestionAnswers.clickQuestionAnswersSearchGo()
        time.sleep(3)

        self.logger.info("************* Searching Text Book **********")

        self.logger.info("********* Search Text Book validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "CBSE" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Search Text Book Test Passed *********")
        elif "Search data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Search Text Book Test Passed because return Search Text Book data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Text Book Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Search Text Book test **********")

    def test_search_QuestionAnswers_with_syllabus_and_class(self, setup):

        self.logger.info("************* Test_09_Search Text Book With Syllabus **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Text Book Test **********")
        self.searchQuestionAnswers = Search(self.driver)
        time.sleep(5)
        self.searchQuestionAnswers.clickOnQuestionAnswersMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Text Book **********")

        searched_value = self.searchQuestionAnswers.drpSyllabus("CBSE")
        time.sleep(3)
        self.searchQuestionAnswers.drpClass("6Th")
        self.searchQuestionAnswers.clickQuestionAnswersSearchGo()
        time.sleep(3)

        self.logger.info("************* Searching Text Book **********")

        self.logger.info("********* Search Text Book validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "6Th" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Search Text Book Test Passed *********")
        elif "Search data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Search Text Book Test Passed because return Search Text Book data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Text Book Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Search Text Book test **********")

    def test_search_QuestionAnswers_with_syllabus_class_and_subject(self, setup):

        self.logger.info("************* Test_09_Search Text Book With Syllabus **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Text Book Test **********")
        self.searchQuestionAnswers = Search(self.driver)
        time.sleep(5)
        self.searchQuestionAnswers.clickOnQuestionAnswersMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Text Book **********")

        searched_value = self.searchQuestionAnswers.drpSyllabus("CBSE")
        time.sleep(3)
        self.searchQuestionAnswers.drpClass("6Th")
        time.sleep(4)
        self.searchQuestionAnswers.drpSubject("Account")
        self.searchQuestionAnswers.clickQuestionAnswersSearchGo()
        time.sleep(3)

        self.logger.info("************* Searching Text Book **********")

        self.logger.info("********* Search Text Book validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Account" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Search Text Book Test Passed *********")
        elif "Text Book data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Search Text Book Test Passed because return Search Text Book data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Text Book Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Search Text Book test **********")

    def test_search_QuestionAnswers(self, setup):

        self.logger.info("************* Test_09_Search Text Book With Syllabus **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Text Book Test **********")
        self.searchQuestionAnswers = Search(self.driver)
        time.sleep(5)
        self.searchQuestionAnswers.clickOnQuestionAnswersMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search **********")

        self.searchQuestionAnswers.setQusAnsSearchBox("How")
        time.sleep(3)
        self.searchQuestionAnswers.clickOnQusAnsSearch()
        time.sleep(3)

        self.logger.info("************* Searching Text Book **********")

        self.logger.info("********* Search Text Book validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "How" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Search Text Book Test Passed *********")
        elif "Question Answer data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Search Text Book Test Passed because return Search Text Book data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Text Book Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Search Text Book test **********")