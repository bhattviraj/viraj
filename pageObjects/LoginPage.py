import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.customLogger import LogGen


class LoginPage:
    # Login Page
    textbox_username_id = "userNameInput"
    textbox_password_id = "passwordInput"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"
    logger = LogGen.loggen()  # Logger

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def verifyLoggedin(self):

        act_home_url = self.driver.current_url
        exp_home_url = "https://tutorpark.ssavts.in/#/home"
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if act_home_url == exp_home_url:
            assert True
        elif "Invalid credentials." in self.msg:
            self.logger.info("************* Login Not successful Invalid credentials**********")
            allure.attach(self.driver.get_screenshot_as_png(), name="TestLoginInvalicredentials",
                          attachment_type=AttachmentType.PNG)
            self.driver.get("https://tutorpark.ssavts.in/#/")
            assert False
        else:
            self.logger.info("************* Login Not successful Something Wrong**********")
            allure.attach(self.driver.get_screenshot_as_png(), name="TestLoginError",
                          attachment_type=AttachmentType.PNG)
            self.driver.get("https://tutorpark.ssavts.in/#/")
            assert False
