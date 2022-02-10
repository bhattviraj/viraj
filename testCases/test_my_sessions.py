import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.NotebookPage import notebook
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_013_notebook:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_search_notebook(self,setup):
        self.logger.info("************* Test_013_search notebook **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search  notebook Test **********")
        self.notebook = notebook(self.driver)
        time.sleep(5)
        self.notebook.clickOnMoreItems() # More Items Menu
        self.notebook.clickOnNotebookMenu() # Click on Menu Item
        time.sleep(5)

        self.logger.info("************* Search  notebook **********")

        searched_value = self.notebook.setSearchNotebook("Literature: ")
        time.sleep(3)
        self.notebook.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching  notebook **********")

        self.logger.info("********* Search  notebook started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Literature: " in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search  notebook Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")