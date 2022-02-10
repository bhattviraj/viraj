import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.QuestionAnswersPage import questionanswers
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
        if 'QuestionS added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Question & Answers Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Question & Answers test **********")

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
        self.QuestionAnswers = AddQuestionAnswers(self.driver)
        time.sleep(5)
        self.QuestionAnswers.clickOnPostSearchJobMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search Question & Answers**********")

        searched_value = self.QuestionAnswers.setSearchJob("viraj")

        self.QuestionAnswers.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search Question & Answers validation started *****************")

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