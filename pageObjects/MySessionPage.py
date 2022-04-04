from selenium.webdriver.common.by import By


class mysessions:
    # My Sessions
    lnkMySession_name = "Sessions"
    txtSearch_xpath="//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickMysessionMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkMySession_name).click()

    def setSearchSession(self, mySession):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(mySession)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
