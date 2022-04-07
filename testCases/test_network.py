import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.NetworkPage import Network
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_021_network:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger
    search_friend = "lina"

    def test_searchfriend(self, setup):
        self.logger.info("************* Test_010_search friend **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.friends = Network(self.driver)
        time.sleep(5)
        self.friends.clickOnNetworkMenu()  # Click on Menu Item
        time.sleep(7)

        self.logger.info("************* Search friend**********")

        self.friends.setSearchNetwork("Dhrumil")
        time.sleep(3)
        self.friends.clickOnSearch()
        time.sleep(3)

        self.logger.info("************* Searching Post **********")

        self.logger.info("********* Search friend validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Dhrumil" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        elif "Network data not available..." in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search friend Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_add_friend(self, setup):
        self.logger.info("************* Test Add friend **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.friends = Network(self.driver)
        time.sleep(5)
        self.friends.clickOnNetworkMenu()  # Click on Menu Item
        time.sleep(7)

        self.logger.info("************* Search friend And Add Friend**********")

        self.friends.clickOnAdd()
        time.sleep(2)

        self.logger.info("************* Searching Post **********")
        self.friends.setNewSearchFriend(self.search_friend)
        time.sleep(3)
        self.logger.info("********* Search friend validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if self.search_friend in self.msg:

            self.friends.clickOnAddSearchFriend()
            time.sleep(3)
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text
            if "Request sent successfully." in self.msg:
                time.sleep(2)
                self.logger.info("******** Test Passed ********")
                assert True
            elif "No records to display" in self.msg:
                time.sleep(2)
                self.logger.info("********** Test Passed********")
                assert False

            else:
                time.sleep(2)
                self.logger.info("********* Test Failed ***********")
                assert False

        elif "No records to display" in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Search friend Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")

    def test_invite_friend(self, setup):
        self.logger.info("************* Test_010_search friend **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Post Test **********")
        self.friends = Network(self.driver)
        time.sleep(5)
        self.friends.clickOnNetworkMenu()  # Click on Menu Item
        time.sleep(7)

        self.logger.info("************* Search friend**********")

        self.friends.clickOnInviteOption()
        time.sleep(2)
        self.friends.setInviteEmail("viraj+111@dasinfomedia.com")
        time.sleep(3)
        self.friends.clickOnInvite()
        time.sleep(3)

        self.logger.info("************* Testing Invite **********")

        self.logger.info("********* validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "Invitaion sent successfully." in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True

        elif "Invitaion already pending." in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True

        elif "User has already been register with this email." in self.msg:
            time.sleep(2)
            self.logger.info("********* Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Network_scr.png")  # Screenshot
            self.logger.error("********* Search friend Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending test **********")
