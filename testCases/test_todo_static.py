import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddTodoPage import AddTodo
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddTodo:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addTodo(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Todo Test **********")
        self.todo = AddTodo(self.driver)
        time.sleep(3)
        self.todo.clickOnTodoMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Providing customer info **********")

        self.todo.setTodo("Test Static")

        self.todo.clickOnAddTodo()
        time.sleep(3)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'Todos added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")
