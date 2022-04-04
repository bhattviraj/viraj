import unittest

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.NotebookPage import notebook
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.sanity
class Test_014_notebook:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_notebook(self, setup):
        self.logger.info("************* Test_014_notebook **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add notebook Test **********")
        self.notebook = notebook(self.driver)
        time.sleep(4)
        self.notebook.clickOnMoreItems()
        time.sleep(2)
        self.notebook.clickOnNotebookMenu()  # Click on Menu Item
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll Page upto Bottom
        time.sleep(4)
        self.notebook.drpSyllabus()
        time.sleep(3)
        self.notebook.drpClass()
        time.sleep(3)
        self.notebook.drpSubject()
        time.sleep(3)
        self.notebook.drpTutor()
        time.sleep(2)

        self.notebook.setDescription("Test notebook")
        time.sleep(4)
        self.notebook.clickOnSubmit()
        time.sleep(3)
        self.logger.info("************* Saving notebook info **********")

        self.logger.info("********* Add notebook validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        exp_alert = "notebook created successfully."
        if 'Notebook added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  notebook Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add notebook Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add notebook test **********")

    def test_searchnotebook(self, setup):
        self.logger.info("************* Test_018_notebook **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search notebook Test **********")
        self.notebook = notebook(self.driver)
        time.sleep(5)
        self.notebook.clickOnMoreItems()
        time.sleep(2)
        self.notebook.clickOnNotebookMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search notebook Job**********")

        searched_value = self.notebook.setSearchNotebook("viraj")

        self.notebook.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching notebook **********")

        self.logger.info("********* Search notebook validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Viraj" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        elif "Notebook data not available..." in self.msg:
            assert True
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Searchnotebook_scr.png")  # Screenshot
            self.logger.error("********* Search notebook Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_DeleteNotebook(self, setup):
        self.logger.info("************* Test_018_notebook **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Delete Notebook Test **********")
        self.notebook = notebook(self.driver)
        time.sleep(5)
        self.notebook.clickOnMoreItems()
        time.sleep(2)
        self.notebook.clickOnNotebookMenu()  # Click on Menu Item
        time.sleep(5)

        self.logger.info("*************Delete Notebook**********")
        self.notebook.clickOnDelete()
        time.sleep(3)
        self.logger.info("*************Delete Notebook **********")

        self.logger.info("*********Delete Notebook validation started *****************")
        self.msg1 = self.driver.find_element(By.TAG_NAME, "body").text
        if "Notebook deleted successfully from database." in self.msg1:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Searchnotebook_scr.png")  # Screenshot
            self.logger.error("*********Delete My Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")
