import time
import unittest

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AdminSubjectsPage import Subjects
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_0018_subjects:
    baseURL = ReadConfig.getApplicationURL()
    adminUsername = ReadConfig.getAdminUseremail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()  # Logger

    def test_subjects(self, setup):
        self.logger.info("************* Test_018_Add_Text_Book **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add subjects Test **********")
        self.subjects = Subjects(self.driver)
        time.sleep(3)
        self.subjects.clickOnSubjectsMenu()  # Click on Menu Item
        time.sleep(4)
        self.subjects.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                popup = handle
                # change the control to page
                self.driver.switch_to.window(popup)
                self.logger.info("************* Providing subjects info **********")

        self.subjects.drpSubject()
        self.subjects.setSubjectsName("GTU")
        self.subjects.setDescription("Test Description")
        self.subjects.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving subjects info **********")

        self.logger.info("********* Add subjects validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'Subject added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  subjects Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add subjects Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add subjects test **********")

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

        self.logger.info("******* Starting Search subjects Test **********")
        self.subjects = Subjects(self.driver)
        time.sleep(5)
        self.subjects.clickOnSubjectsMenu()
        time.sleep(3)

        self.logger.info("************* Search subjects **********")

        self.subjects.setSearchSubjects("CBSE")
        time.sleep(3)

        self.logger.info("************* Searching subjects **********")

        self.logger.info("********* Search subjects  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_subjects_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_subjects_name(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search subjects Test **********")
        self.subjects = Subjects(self.driver)
        time.sleep(5)
        self.subjects.clickOnSubjectsMenu()
        time.sleep(3)

        self.logger.info("************* Search subjects **********")

        self.subjects.setSearchSubjectsName("Hindi")
        time.sleep(2)

        self.logger.info("************* Searching subjects **********")

        self.logger.info("********* Search subjects  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Hindi" in self.msg:

            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True

        elif "No records to display" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_subjects_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_subjects_created_date(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search subjects Test **********")
        self.subjects = Subjects(self.driver)
        time.sleep(5)
        self.subjects.clickOnSubjectsMenu()
        time.sleep(3)

        self.logger.info("************* Search subjects **********")

        self.subjects.setSearchSubjectsCreatedDate("02-04-2022")
        time.sleep(2)

        self.logger.info("************* Searching subjects **********")

        self.logger.info("********* Search subjects  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_subjects_scr.png")  # Screenshot
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

        self.logger.info("******* Starting Search subjects Test **********")
        self.subjects = Subjects(self.driver)
        time.sleep(5)
        self.subjects.clickOnSubjectsMenu()
        time.sleep(3)

        self.logger.info("************* Search subjects **********")

        self.subjects.setSearchSubjects("GTU")
        time.sleep(2)

        self.logger.info("************* Searching subjects **********")

        self.logger.info("********* Search subjects  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "GTU" in self.msg:

            time.sleep(2)
            self.subjects.clickOnDelete()
            time.sleep(2)

            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if "Subject deleted from database." in self.msg:
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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_subjects_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")
