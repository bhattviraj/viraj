import unittest

import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.TextBookPage import TextBook
from pageObjects.SearchDataPage import Search
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_0009_TextBook:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_TextBook(self, setup):
        self.logger.info("************* Test_009_Add_Text_Book **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Text Book Test **********")
        self.textbook =TextBook(self.driver)
        time.sleep(3)
        self.textbook.clickOnTextBookMenu() #Click on Menu Item
        time.sleep(4)
        self.textbook.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                popup = handle
                # change the control to page
                self.driver.switch_to.window(popup)
                self.logger.info("************* Providing Text Book info **********")

        self.textbook.drpSyllabus()
        time.sleep(3)
        self.textbook.drpClass()
        time.sleep(3)
        self.textbook.drpSubject()
        time.sleep(2)
        self.textbook.setBookName("Network")
        self.textbook.setBookImage("D:/Documents/Downloads/network.jpg")
        self.textbook.setExternalLink("http://www.africau.edu/images/default/sample.pdf")
        self.textbook.setDescription("Test Description")
        self.textbook.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving Text Book info **********")

        self.logger.info("********* Add Textbook validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'Textbook added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Text Book Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add Text Book Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Text Book test **********")

    def test_search_textbook_with_syllabus(self, setup):

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
            self.searchtextbook = Search(self.driver)
            time.sleep(5)
            self.searchtextbook.clickOnTextBookMenu()  # Click on Menu Item
            time.sleep(4)

            self.logger.info("************* Search Text Book **********")

            self.searchtextbook.drpSyllabus("CBSE")

            self.searchtextbook.clickTextBookSearchGo()
            time.sleep(3)

            self.logger.info("************* Searching Text Book **********")

            self.logger.info("********* Search Text Book validation started *****************")

            self.msg = self.driver.find_element_by_tag_name("body").text

            if "CBSE" in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Search Text Book Test Passed *********")
            elif "Search data not available..." in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Search Text Book Test Passed because return Search Text Book data not available...*********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
                self.logger.error("********* Search Text Book Test Failed ************")
                assert False

            self.driver.close()
            self.logger.info("******* Ending Search Text Book test **********")

    def test_search_textbook_with_syllabus_and_class(self, setup):

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
            self.searchtextbook = Search(self.driver)
            time.sleep(5)
            self.searchtextbook.clickOnTextBookMenu()  # Click on Menu Item
            time.sleep(4)

            self.logger.info("************* Search Text Book **********")

            searched_value = self.searchtextbook.drpSyllabus("CBSE")
            time.sleep(3)
            self.searchtextbook.drpClass("10th")
            self.searchtextbook.clickTextBookSearchGo()
            time.sleep(3)

            self.logger.info("************* Searching Text Book **********")

            self.logger.info("********* Search Text Book validation started *****************")

            self.msg = self.driver.find_element_by_tag_name("body").text
            print(self.msg)

            if "10th" in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Search Text Book Test Passed *********")
            elif "Search data not available..." in self.msg:
                assert True
                time.sleep(2)
                self.logger.info("********* Search Text Book Test Passed because return Search Text Book data not available...*********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
                self.logger.error("********* Search Text Book Test Failed ************")
                assert False

            self.driver.close()
            self.logger.info("******* Ending Search Text Book test **********")

    def test_search_textbook_with_syllabus_class_and_subject(self, setup):

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
            self.searchtextbook = Search(self.driver)
            time.sleep(5)
            self.searchtextbook.clickOnTextBookMenu()  # Click on Menu Item
            time.sleep(4)

            self.logger.info("************* Search Text Book **********")

            searched_value = self.searchtextbook.drpSyllabus("CBSE")
            time.sleep(3)
            self.searchtextbook.drpClass("10th")
            time.sleep(3)
            self.searchtextbook.drpSubject("Network")
            self.searchtextbook.clickTextBookSearchGo()
            time.sleep(3)

            self.logger.info("************* Searching Text Book **********")

            self.logger.info("********* Search Text Book validation started *****************")

            self.msg = self.driver.find_element_by_tag_name("body").text
            print(self.msg)

            if "History" in self.msg:
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

    def test_search_textbook_with_(self, setup):

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
            self.searchtextbook = Search(self.driver)
            time.sleep(5)
            self.searchtextbook.clickOnTextBookMenu()  # Click on Menu Item
            time.sleep(4)

            self.logger.info("************* Search Text Book **********")

            searched_value = self.searchtextbook.setSearchByBookName("Network")

            self.searchtextbook.clickTextBookSearchGo()
            time.sleep(3)

            self.logger.info("************* Searching Text Book **********")

            self.logger.info("********* Search Text Book validation started *****************")

            self.msg = self.driver.find_element_by_tag_name("body").text

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

    def test_delete_textbook(self, setup):

        self.logger.info("************* Test_154_Delete Text Book**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Delete Text Book Test **********")
        self.delete_textbook = TextBook(self.driver)
        time.sleep(5)
        self.delete_textbook.clickOnTextBookMenu()  # Click on Menu Item
        time.sleep(4)

        self.delete_textbook.clickOnOption()
        time.sleep(2)
        self.delete_textbook.clickOnDelete()

        self.logger.info("********* Delete Text Book validation started *****************")
        time.sleep(3)
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "TextBook deleted from database." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Delete Text Book Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search Text Book Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Delete Text Book test **********")