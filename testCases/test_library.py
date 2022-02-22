import unittest

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.LibraryPage import Library
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_019_library:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    #@pytest.mark.sanity
    def test_library(self, setup):
        self.logger.info("************* Test_014_library **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add library Test **********")
        self.library = Library(self.driver)
        time.sleep(3)
        self.library.clickOnMoreItems()
        time.sleep(2)
        self.library.clickOnLibraryMenu() # Click on Menu Item
        time.sleep(5)
        self.library.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access Add library page
        for handle in self.driver.window_handles:
            if handle != main_page:
                page = handle
                # change the control to Add library page
                self.driver.switch_to.window(page)
                self.logger.info("************* Providing library info **********")

        self.library.setTitle("library Demo")
        self.library.drpSyllabus()
        time.sleep(3)
        self.library.drpClass()
        time.sleep(3)
        self.library.drpSubject()
        time.sleep(2)
        self.library.setLibraryAttachment("D:/Documents/Downloads/network.jpg")
        time.sleep(2)
        self.library.setLibraryImage("D:/Documents/Downloads/network.jpg")
        self.library.setDescription("Test library")
        time.sleep(4)
        self.library.clickOnSubmit()
        time.sleep(6)
        self.logger.info("************* Saving library info **********")

        self.logger.info("********* Add library validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        exp_alert = "library created successfully."
        # act_alert = self.driver.find_element_by_xpath("//div[2]")
        if 'Library added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  library Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addlibrary_scr.png")  # Screenshot
            self.logger.error("********* Add library Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add library test **********")

    #@pytest.mark.sanity
    def test_searchlibrary(self, setup):
        self.logger.info("************* Test_014_library **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add library Test **********")
        self.library = Library(self.driver)
        time.sleep(3)
        self.library.clickOnMoreItems()
        time.sleep(2)
        self.library.clickOnLibraryMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search library**********")

        searched_value = self.library.setSearchlibrary("English")
        time.sleep(3)
        self.library.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search library validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "English" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        elif "library data not available..." in self.msg:
            assert True
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addlibrary_scr.png")  # Screenshot
            self.logger.error("********* Search library Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    #@pytest.mark.sanity
    def test_search_library_with_syllabus(self, setup):
        self.logger.info("************* Test_014_library **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add library Test **********")
        self.library = Library(self.driver)
        time.sleep(3)
        self.library.clickOnMoreItems()
        time.sleep(2)
        self.library.clickOnLibraryMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search library**********")

        self.library.drpSearchSyllabus("CBSE")

        self.library.clickOnGo()
        time.sleep(3)
        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search library validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "CBSE" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        elif "Library data not available..." in self.msg:
            assert True
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addlibrary_scr.png")  # Screenshot
            self.logger.error("********* Search library Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    #@pytest.mark.sanity
    def test_search_library_with_syllabus_and_class(self, setup):
        self.logger.info("************* Test_014_library **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add library Test **********")
        self.library = Library(self.driver)
        time.sleep(3)
        self.library.clickOnMoreItems()
        time.sleep(2)
        self.library.clickOnLibraryMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search library**********")

        self.library.drpSearchSyllabus("CBSE")
        time.sleep(3)
        self.library.drpSearchClass("10th")
        time.sleep(3)
        self.library.clickOnGo()
        time.sleep(3)
        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search library validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "10th" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        elif "Library data not available..." in self.msg:
            assert True
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addlibrary_scr.png")  # Screenshot
            self.logger.error("********* Search library Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    #@pytest.mark.sanity
    def test_search_library_with_syllabus_class_and_subject(self, setup):
        self.logger.info("************* Test_014_library **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add library Test **********")
        self.library = Library(self.driver)
        time.sleep(3)
        self.library.clickOnMoreItems()
        time.sleep(2)
        self.library.clickOnLibraryMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search library**********")

        self.library.drpSearchSyllabus("CBSE")
        time.sleep(3)
        self.library.drpSearchClass("10th")
        time.sleep(3)
        self.library.drpSearchSubject("Science")
        time.sleep(3)
        self.library.clickOnGo()
        time.sleep(3)
        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search library validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Science" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        elif "Library data not available..." in self.msg:
            assert True
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addlibrary_scr.png")  # Screenshot
            self.logger.error("********* Search library Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    #@pytest.mark.sanity
    def test_Deletelibrary(self, setup):
        self.logger.info("************* Test_018_library **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Delete library Test **********")
        self.library = Library(self.driver)
        time.sleep(5)
        self.library.clickOnMoreItems()
        time.sleep(2)
        self.library.clickOnLibraryMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("*************Delete library**********")

        self.library.clickOnLibraryOption()
        time.sleep(3)
        self.library.clickOnLibraryDelete()
        time.sleep(3)
        self.logger.info("*************Delete library **********")

        self.logger.info("*********Delete library validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Library deleted from database." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Searchlibrary_scr.png")  # Screenshot
            self.logger.error("*********Delete My Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")