import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.SignupPage import Signup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_signup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_signup(self, setup):
        self.logger.info("************* Test_003_Signup **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.get("http://tutorpark.ssavts.in/#/register")
        self.logger.info("******* Starting Signup **********")
        self.signup = Signup(self.driver)
        time.sleep(5)

        self.logger.info("************* Providing customer info **********")

        self.signup.setFirstname("Viraj")
        self.signup.setLastname("Bhatt")
        self.signup.setEmail("viraj75@dasinfomedia.com")
        self.signup.setPhone("8965437643")
        self.signup.setAadhar_id("1234567890123456")
        self.signup.setPassword("Viraj123")
        self.signup.setConfirmPassword("Viraj123")
        self.signup.setAdress("Address Ahmedabad")
        self.signup.setDrpState("Gujarat")
        self.signup.setCity("Ahmedabad")
        self.signup.setPincode("123456")
        time.sleep(2)
        self.signup.clickOnSignup()
        time.sleep(3)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        exp_url = "http://tutorpark.ssavts.in/#/register-successs"
        act_url = self.driver.current_url

        if exp_url == act_url:
            assert True
            self.logger.info("********* Signup Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Signup Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Signup test **********")
