import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddTodoPage import AddTodo
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_003_DDT_AddTodo():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/TodoData.xlsx"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

   # @pytest.mark.regression
    def test_addTodo_ddt(self, setup):
        self.logger.info("************* Test_003_AddTodo **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("************* Login Successful **********")

        self.logger.info("******* Starting Add Todo Test **********")
        self.todo = AddTodo(self.driver)

        self.todo.clickOnTodoMenu() #Click on Menu Item
        time.sleep(4)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.task = XLUtils.readData(self.path, 'Sheet1', r, 1)
            time.sleep(4)
            self.todo.setTodo(self.task)

            self.todo.clickOnAddTodo()
            time.sleep(3)

            self.msg = self.driver.find_element_by_tag_name("div").text
            print(self.msg)
            lst_status.append("Todos added successfully in the database.")
        if 'Todos added successfully in the database.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")
