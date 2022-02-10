import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.FindTutorPage import FindTutor
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string

class Test_006_FindTutor:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_findtutor(self,setup):
        self.logger.info("************* Test_006_FindTutor **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu() # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutorpark**********")

        searched_value = self.findtutor.setSearchbox("viraj")

        self.findtutor.clickSearch()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "viraj" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

    def test_findtuor_with_city(self,setup):

        self.logger.info("************* Test_006_Find tutor with city **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutorpark**********")

        searched_value = self.findtutor.setSearchboxCity("viraj")

        self.findtutor.clickg()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "viraj" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Find Tutor Test Passed *********")
        elif "Find Tutor data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Find Tutor Test Passed because return Find Tutor data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Find Tutor test **********")

    def test_findtuor_with_syllabus(self, setup):

        self.logger.info("************* Test_006_Find tutor with city **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutorpark**********")

        searched_value = self.findtutor.drpSyllabus("CBSE")

        self.findtutor.clickg()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "CBSE" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Find Tutor Test Passed *********")
        elif "Find Tutor data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Find Tutor Test Passed because return Find Tutor data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Find Tutor test **********")

    def test_findtuor_with_syllabus_and_class(self, setup):

        self.logger.info("************* Test_006_Find tutor with city **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutorpark**********")

        searched_value = self.findtutor.drpSyllabus("CBSE")
        time.sleep(2)
        self.findtutor.drpClass("10th")

        self.findtutor.clickg()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "10th" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Find Tutor Test Passed *********")
        elif "Find Tutor data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Find Tutor Test Passed because return Find Tutor data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Find Tutor test **********")

    def test_findtuor_with_syllabus_class_and_subject(self, setup):

        self.logger.info("************* Test_006_Find tutor with city **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutorpark**********")

        searched_value = self.findtutor.drpSyllabus("CBSE")
        time.sleep(2)
        self.findtutor.drpClass("10th")
        time.sleep(2)
        self.findtutor.drpSubject("Network")
        self.findtutor.clickg()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Network" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Find Tutor Test Passed *********")
        elif "Find Tutor data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Find Tutor Test Passed because return Find Tutor data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Find Tutor test **********")
    def test_findtuor_with_mode(self, setup):

        self.logger.info("************* Test_006_Find tutor with city **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutor**********")

        searched_value = self.findtutor.drpMode("Online")

        self.findtutor.clickg()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Online" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Find Tutor Test Passed *********")
        elif "Find Tutor data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Find Tutor Test Passed because return Find Tutor data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Find Tutor test **********")

    def test_findtuor_with_gender(self, setup):

        self.logger.info("************* Test_006_Find tutor with city **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutor**********")

        searched_value = self.findtutor.drpGender("Male")

        self.findtutor.clickg()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "Male" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Find Tutor Test Passed *********")
        elif "Find Tutor data not available..." in self.msg:
            assert True
            time.sleep(2)
            self.logger.info(
                "********* Find Tutor Test Passed because return Find Tutor data not available...*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Find Tutor test **********")

    def test_findtutor_with_Experience(self, setup):
        self.logger.info("************* Test_006_FindTutor **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Find Tutor Test **********")
        self.findtutor = FindTutor(self.driver)
        time.sleep(5)
        self.findtutor.clickOnFindTutorMenu()  # Click on Menu Item
        time.sleep(4)

        self.logger.info("************* Search Tutorpark**********")

        searched_value = self.findtutor.setExperience("1")

        self.findtutor.clickg()
        time.sleep(3)

        self.logger.info("************* Searching Tutor **********")

        self.logger.info("********* Find Tutor validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "1" in self.msg:
            assert True
            time.sleep(2)
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Find Tutor Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")