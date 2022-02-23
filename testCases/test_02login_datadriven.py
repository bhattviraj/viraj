import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

@pytest.mark.sanity
@allure.title("Login Testcases")
class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    def test_login_ddt(self, setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_home_url = self.driver.current_url
            exp_home_url = "http://tutorpark.ssavts.in/#/home"

            if act_home_url == exp_home_url:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout()
                    lst_status.append("Pass1")
                elif self.exp == 'Fail':
                    allure.attach(self.driver.get_screenshot_as_png(), name="TestTodoScreen",
                                  attachment_type=AttachmentType.PNG)
                    self.logger.info("**** failed ****")
                    self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_home_url != exp_home_url:
                if self.exp == 'Pass':
                    allure.attach(self.driver.get_screenshot_as_png(), name="TestTodoScreen",
                                  attachment_type=AttachmentType.PNG)
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass2")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");
