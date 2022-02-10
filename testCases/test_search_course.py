import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchDataPage import Search
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string

class Test_007_searchCourse:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_searchcourse(self,setup):
        self.logger.info("************* Test_006_searchcourse **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Course Test **********")
        self.searchcourse = Search(self.driver)
        time.sleep(5)
        self.searchcourse.clickOnSearchCourseMenu() # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Coursepark**********")

        searched_value = self.searchcourse.setSearchbox("My Course")

        self.searchcourse.clickSearch()
        time.sleep(3)

        self.logger.info("************* Searching Course **********")

        self.logger.info("********* Search Coursetor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "My Course" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

    def test_search_course_with_syllabus(self, setup):

            self.logger.info("************* Test_006_Search Coursetor with city **********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.logger.info("************* Login successful **********")

            self.logger.info("******* Starting Search Coursetor Test **********")
            self.searchcourse = Search(self.driver)
            time.sleep(5)
            self.searchcourse.clickOnSearchCourseMenu()  # Click on Menu Item
            time.sleep(4)

            self.logger.info("************* Search Coursepark**********")

            searched_value = self.searchcourse.drpSyllabus("CBSE")

            self.searchcourse.clickg()
            time.sleep(3)

            self.logger.info("************* Searching Course **********")

            self.logger.info("********* Search Coursetor validation started *****************")

            self.msg = self.driver.find_element_by_tag_name("body").text
            print(self.msg)

            if "CBSE" in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Search Coursetor Test Passed *********")
            elif "Search Coursetor data not available..." in self.msg:
                assert True
                time.sleep(2)
                self.logger.info(
                    "********* Search Coursetor Test Passed because return Search Coursetor data not available...*********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
                self.logger.error("********* Search Coursetor Test Failed ************")
                assert False

            self.driver.close()
            self.logger.info("******* Ending Search Coursetor test **********")

    def test_search_course_with_syllabus_and_class(self, setup):

            self.logger.info("************* Test_006_Search Coursetor with city **********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.logger.info("************* Login successful **********")

            self.logger.info("******* Starting Search Coursetor Test **********")
            self.searchcourse = Search(self.driver)
            time.sleep(5)
            self.searchcourse.clickOnSearchCourseMenu()  # Click on Menu Item
            time.sleep(4)

            self.logger.info("************* Search Coursepark**********")

            searched_value = self.searchcourse.drpSyllabus("CBSE")
            time.sleep(2)
            self.searchcourse.drpClass("10th")

            self.searchcourse.clickg()
            time.sleep(3)

            self.logger.info("************* Searching Course **********")

            self.logger.info("********* Search Coursetor validation started *****************")

            self.msg = self.driver.find_element_by_tag_name("body").text
            print(self.msg)

            if "10th" in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Search Coursetor Test Passed *********")
            elif "Search Coursetor data not available..." in self.msg:
                assert True
                time.sleep(2)
                self.logger.info(
                    "********* Search Coursetor Test Passed because return Search Coursetor data not available...*********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
                self.logger.error("********* Search Coursetor Test Failed ************")
                assert False

            self.driver.close()
            self.logger.info("******* Ending Search Coursetor test **********")

    def test_search_course_with_syllabus_class_and_subject(self, setup):

            self.logger.info("************* Test_006_Search Coursetor with city **********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.logger.info("************* Login successful **********")

            self.logger.info("******* Starting Search Coursetor Test **********")
            self.searchcourse = Search(self.driver)
            time.sleep(5)
            self.searchcourse.clickOnSearchCourseMenu()  # Click on Menu Item
            time.sleep(4)

            self.logger.info("************* Search Coursepark**********")

            searched_value = self.searchcourse.drpSyllabus("CBSE")
            time.sleep(2)
            self.searchcourse.drpClass("10th")
            time.sleep(2)
            self.searchcourse.drpSubject("Network")
            self.searchcourse.clickg()
            time.sleep(3)

            self.logger.info("************* Searching Course **********")

            self.logger.info("********* Search Coursetor validation started *****************")

            self.msg = self.driver.find_element_by_tag_name("body").text
            print(self.msg)

            if "Network" in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Search Coursetor Test Passed *********")
            elif "Search Coursetor data not available..." in self.msg:
                assert True
                time.sleep(2)
                self.logger.info(
                    "********* Search Coursetor Test Passed because return Search Coursetor data not available...*********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
                self.logger.error("********* Search Coursetor Test Failed ************")
                assert False

            self.driver.close()
            self.logger.info("******* Ending Add customer test **********")