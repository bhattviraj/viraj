import pytest
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageObjects.SignupPage import Signup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@allure.title("Signup Testcase")
@pytest.mark.sanity
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
        time.sleep(10)

        self.logger.info("************* Providing customer info **********")

        self.signup.setFirstname("Viraj")
        self.signup.setLastname("Bhatt")
        self.signup.setEmail("viraj12@dasinfomedia.com")
        self.signup.setPhone("8965437643")
        self.signup.setAadhar_id("123456789012")
        self.signup.setPassword("Viraj123")
        self.signup.setConfirmPassword("Viraj123")
        self.signup.setAdress("Address Ahmedabad")
        self.signup.setDrpState("Gujarat")
        self.signup.setCity("Ahmedabad")
        self.signup.setPincode("123456")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll Page upto Bottom
        time.sleep(2)
        self.signup.clickOnSignup()
        time.sleep(3)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* validation started *****************")

        exp_url = "http://tutorpark.ssavts.in/#/register-success"
        act_url = self.driver.current_url
        exp_alert = "The email has already been taken."
        act_alert = print(self.driver.find_element(By.XPATH, "//div[2]").text)

        if exp_url == act_url:
            assert True
            self.logger.info("********* Signup Test Passed *********")

        elif exp_alert == act_alert:
            assert True
            self.logger.info("********* Signup Test Passed *********")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestSignupScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Signup Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Signup test **********")
