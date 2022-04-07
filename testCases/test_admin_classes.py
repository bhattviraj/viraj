import time
import unittest

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AdminClassPage import ClassData
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_0018_Classes:
    baseURL = ReadConfig.getApplicationURL()
    adminUsername = ReadConfig.getAdminUseremail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()  # Logger

    def test_Classes(self, setup):
        self.logger.info("************* Test_018_Add_Text_Book **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Classes Test **********")
        self.classes = ClassData(self.driver)
        time.sleep(3)
        self.classes.clickOnClassDataMenu()  # Click on Menu Item
        time.sleep(4)
        self.classes.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                popup = handle
                # change the control to page
                self.driver.switch_to.window(popup)
                self.logger.info("************* Providing Classes info **********")

        self.classes.drpSyllabus()
        time.sleep(2)
        self.classes.setClassDataName("GTU")
        self.classes.drpLevel()
        time.sleep(2)
        self.classes.setDescription("Test Description")
        time.sleep(2)
        self.classes.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving Classes info **********")

        self.logger.info("********* Add Classes validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'Class added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Classes Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add Classes Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Classes test **********")

    def test_search(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search ClassData Test **********")
        self.ClassData = ClassData(self.driver)
        time.sleep(5)
        self.ClassData.clickOnClassDataMenu()
        time.sleep(3)

        self.logger.info("************* Search ClassData **********")

        self.ClassData.setSearchClassData("6th")
        time.sleep(2)

        self.logger.info("************* Searching ClassData **********")

        self.logger.info("********* Search ClassData  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "6Th" in self.msg:

            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True

        elif "No records to display" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_ClassData_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_ClassData_name(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search ClassData Test **********")
        self.ClassData = ClassData(self.driver)
        time.sleep(5)
        self.ClassData.clickOnClassDataMenu()
        time.sleep(3)

        self.logger.info("************* Search ClassData **********")

        self.ClassData.setSearchClassDataName("CBSE")
        time.sleep(2)

        self.logger.info("************* Searching ClassData **********")

        self.logger.info("********* Search ClassData  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "CBSE" in self.msg:

            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True

        elif "No records to display" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_ClassData_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_ClassData_created_date(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search ClassData Test **********")
        self.ClassData = ClassData(self.driver)
        time.sleep(5)
        self.ClassData.clickOnClassDataMenu()
        time.sleep(3)

        self.logger.info("************* Search ClassData **********")

        self.ClassData.setSearchClassDataCreatedDate("02-04-2022")
        time.sleep(2)

        self.logger.info("************* Searching ClassData **********")

        self.logger.info("********* Search ClassData  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "02-04-2022" in self.msg:

            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True

        elif "No records to display" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_ClassData_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_delete(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search ClassData Test **********")
        self.ClassData = ClassData(self.driver)
        time.sleep(5)
        self.ClassData.clickOnClassDataMenu()
        time.sleep(3)

        self.logger.info("************* Search ClassData **********")

        self.ClassData.setSearchClassData("GTU")
        time.sleep(2)

        self.logger.info("************* Searching ClassData **********")

        self.logger.info("********* Search ClassData  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "GTU" in self.msg:

            time.sleep(2)
            self.ClassData.clickOnDelete()
            time.sleep(2)

            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if "Class deleted from database." in self.msg:
                self.logger.info("********* Test Passed *********")
                assert True
            else:
                self.logger.info("********* Test Field *********")
                assert False

        elif "No records to display" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_ClassData_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")
