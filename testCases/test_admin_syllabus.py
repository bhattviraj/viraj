import time
import unittest

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AdminSyllabusPage import Syllabus
from pageObjects.SearchDataPage import Search
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_0018_Syllabus:
    baseURL = ReadConfig.getApplicationURL()
    adminUsername = ReadConfig.getAdminUseremail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()  # Logger

    def test_Syllabus(self, setup):
        self.logger.info("************* Test_018_Add_Text_Book **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Syllabus Test **********")
        self.Syllabus = Syllabus(self.driver)
        time.sleep(3)
        self.Syllabus.clickOnSyllabusMenu()  # Click on Menu Item
        time.sleep(4)
        self.Syllabus.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                popup = handle
                # change the control to page
                self.driver.switch_to.window(popup)
                self.logger.info("************* Providing Syllabus info **********")

        self.Syllabus.setSyllabusName("GTU")
        self.Syllabus.setDescription("Test Description")
        self.Syllabus.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving Syllabus info **********")

        self.logger.info("********* Add Syllabus validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'Syllabus added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Syllabus Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add Syllabus Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Syllabus test **********")

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

        self.logger.info("******* Starting Search Syllabus Test **********")
        self.syllabus = Syllabus(self.driver)
        time.sleep(5)
        self.syllabus.clickOnSyllabusMenu()
        time.sleep(3)

        self.logger.info("************* Search Syllabus **********")

        self.syllabus.setSearchSyllabus("CBSE")
        time.sleep(2)

        self.logger.info("************* Searching Syllabus **********")

        self.logger.info("********* Search Syllabus  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Syllabus_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_syllabus_name(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Syllabus Test **********")
        self.syllabus = Syllabus(self.driver)
        time.sleep(5)
        self.syllabus.clickOnSyllabusMenu()
        time.sleep(3)

        self.logger.info("************* Search Syllabus **********")

        self.syllabus.setSearchSyllabusName("CBSE")
        time.sleep(2)

        self.logger.info("************* Searching Syllabus **********")

        self.logger.info("********* Search Syllabus  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Syllabus_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_syllabus_created_date(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Syllabus Test **********")
        self.syllabus = Syllabus(self.driver)
        time.sleep(5)
        self.syllabus.clickOnSyllabusMenu()
        time.sleep(3)

        self.logger.info("************* Search Syllabus **********")

        self.syllabus.setSearchSyllabusCreatedDate("02-04-2022")
        time.sleep(2)

        self.logger.info("************* Searching Syllabus **********")

        self.logger.info("********* Search Syllabus  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Syllabus_scr.png")  # Screenshot
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

        self.logger.info("******* Starting Search Syllabus Test **********")
        self.syllabus = Syllabus(self.driver)
        time.sleep(5)
        self.syllabus.clickOnSyllabusMenu()
        time.sleep(3)

        self.logger.info("************* Search Syllabus **********")

        self.syllabus.setSearchSyllabus("GTU")
        time.sleep(2)

        self.logger.info("************* Searching Syllabus **********")

        self.logger.info("********* Search Syllabus  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "GTU" in self.msg:

            time.sleep(2)
            self.syllabus.clickOnDelete()
            time.sleep(2)

            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if "Syllabus deleted from database." in self.msg:
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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Syllabus_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")
