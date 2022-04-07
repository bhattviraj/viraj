import time
import unittest

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AdminLevelsPage import Level
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_0018_Levels:
    baseURL = ReadConfig.getApplicationURL()
    adminUsername = ReadConfig.getAdminUseremail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()  # Logger

    def test_Levels(self, setup):
        self.logger.info("************* Test_018_Add_Text_Book **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Levels Test **********")
        self.Levels = Level(self.driver)
        time.sleep(3)
        self.Levels.clickOnLevelMenu()  # Click on Menu Item
        time.sleep(4)
        self.Levels.clickOnAdd()  # Click On Add Button
        time.sleep(4)
        main_page = self.driver.current_window_handle
        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != main_page:
                popup = handle
                # change the control to page
                self.driver.switch_to.window(popup)
                self.logger.info("************* Providing Levels info **********")

        self.Levels.setLevelName("GTU")
        self.Levels.setDescription("Test Description")
        self.Levels.clickOnSubmit()
        time.sleep(3)

        self.logger.info("************* Saving Levels info **********")

        self.logger.info("********* Add Levels validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'Level added successfully in the database.' in self.msg:
            assert True
            time.sleep(3)
            self.logger.info("********* Add  Levels Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add Levels Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Levels test **********")

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

        self.logger.info("******* Starting Search Levels Test **********")
        self.Levels = Level(self.driver)
        time.sleep(5)
        self.Levels.clickOnLevelMenu()
        time.sleep(3)

        self.logger.info("************* Search Levels **********")

        self.Levels.setSearchLevelName("CBSE")
        time.sleep(2)

        self.logger.info("************* Searching Levels **********")

        self.logger.info("********* Search Levels  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Levels_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_Levels_name(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Levels Test **********")
        self.Levels = Level(self.driver)
        time.sleep(5)
        self.Levels.clickOnLevelMenu()
        time.sleep(3)

        self.logger.info("************* Search Levels **********")

        self.Levels.setSearchLevelName("CBSE")
        time.sleep(2)

        self.logger.info("************* Searching Levels **********")

        self.logger.info("********* Search Levels  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Levels_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_search_Levels_created_date(self, setup):
        self.logger.info("************* Test_008_search  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.adminUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Levels Test **********")
        self.Levels = Level(self.driver)
        time.sleep(5)
        self.Levels.clickOnLevelMenu()
        time.sleep(3)

        self.logger.info("************* Search Levels **********")

        self.Levels.setSearchLevelCreatedDate("02-04-2022")
        time.sleep(2)

        self.logger.info("************* Searching Levels **********")

        self.logger.info("********* Search Levels  validation started *****************")

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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Levels_scr.png")  # Screenshot
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

        self.logger.info("******* Starting Search Levels Test **********")
        self.Levels = Level(self.driver)
        time.sleep(5)
        self.Levels.clickOnLevelMenu()
        time.sleep(3)

        self.logger.info("************* Search Levels **********")

        self.Levels.setSearchLevel("GTU")
        time.sleep(2)

        self.logger.info("************* Searching Levels **********")

        self.logger.info("********* Search Levels  validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "GTU" in self.msg:

            time.sleep(2)
            self.Levels.clickOnDelete()
            time.sleep(2)

            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if "Level deleted from database." in self.msg:
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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Levels_scr.png")  # Screenshot
            self.logger.error("********* Search Coursetor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")
