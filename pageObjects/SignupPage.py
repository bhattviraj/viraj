import time
from selenium import webdriver
from utilities import XLUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Signup:
    # Signup
    #lnk_menu_name = ""
    txtFirstName_name = "first_name"
    txtLastName_name = "last_name"
    txtEmail_name = "email"
    txtPhone_name = "phone"
    txtAadharId_name = "aadhar_id"
    txtPassword_name = "password"
    txtConfirPassword_name = "password_confirmation"
    txtAddress_name = "address"

    # Select State Dropdown code
    drpState_xpath = "//div[@id='root']/div/div/div/div/div/div[2]/div/form/div[9]/div/div/div/div/input"
    # Select City
    drpCity_xpath = "//div[@id='root']/div/div/div/div/div/div[2]/div/form/div[9]/div[2]/div/div/div/input"

    txtPincode_name = "pincode"
    btnSignup_xpath = "//div[@id='root']/div/div/div/div/div/div[2]/div/form/div[11]/div/div/button"

    def __init__(self, driver):
        self.driver = driver

    #def clickOnTodoMenu(self):
    #    self.driver.find_element_by_link_text(self.lnkTodo_menu_name).click()

    def setFirstname(self, firstname):
        self.driver.find_element_by_name(self.txtFirstName_name).clear()
        self.driver.find_element_by_name(self.txtFirstName_name).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_name(self.txtLastName_name).clear()
        self.driver.find_element_by_name(self.txtLastName_name).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element_by_name(self.txtEmail_name).clear()
        self.driver.find_element_by_name(self.txtEmail_name).send_keys(email)

    def setPhone(self, phone):
        self.driver.find_element_by_name(self.txtPhone_name).clear()
        self.driver.find_element_by_name(self.txtPhone_name).send_keys(phone)

    def setAadhar_id(self, aadhar_id):
        self.driver.find_element_by_name(self.txtAadharId_name).clear()
        self.driver.find_element_by_name(self.txtAadharId_name).send_keys(aadhar_id)


    def setPassword(self, password):
        self.driver.find_element_by_name(self.txtPassword_name).clear()
        self.driver.find_element_by_name(self.txtPassword_name).send_keys(password)

    def setConfirmPassword(self, confirmpassword):
        self.driver.find_element_by_name(self.txtConfirPassword_name).clear()
        self.driver.find_element_by_name(self.txtConfirPassword_name).send_keys(confirmpassword)

    def setAdress(self, address):
        self.driver.find_element_by_name(self.txtAddress_name).clear()
        self.driver.find_element_by_name(self.txtAddress_name).send_keys(address)

    def setDrpState(self, drpstate):
        drpsate_save= self.driver.find_element(By.XPATH, self.drpState_xpath)

        self.driver.execute_script("arguments[0].click();", drpsate_save)
        # select From Auto Auggestion value
        drpsate_save.send_keys(drpstate)
        drpsate_save.send_keys(Keys.ARROW_DOWN)
        drpsate_save.send_keys(Keys.ENTER)

    def setCity(self, drpcity):
        drpcity_save = self.driver.find_element(By.XPATH, self.drpCity_xpath)
        self.driver.execute_script("arguments[0].click();", drpcity_save)
        # select From Auto Auggestion value
        drpcity_save.send_keys(drpcity)
        drpcity_save.send_keys(Keys.ARROW_DOWN)
        drpcity_save.send_keys(Keys.ENTER)

    def setPincode(self, pincode):
        self.driver.find_element_by_name(self.txtPincode_name).clear()
        self.driver.find_element_by_name(self.txtPincode_name).send_keys(pincode)

    def clickOnSignup(self):
        self.driver.find_element_by_xpath(self.btnSignup_xpath).click()
