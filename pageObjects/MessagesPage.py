from selenium.webdriver.common.by import By


class Messages:
    # Messages
    lnkMessages_menu_name = "Messages"
    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]/div"
    btnUserTab_xpath = "//*[@id='mui-p-16048-P-1']/div/div"
    txtMessage_xpath = "//*[@id='body']"
    btnSendMessage_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/form/div/div/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMessagaesMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkMessages_menu_name).click()

    def setSearch(self, messages):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(messages)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def clickOnUserChat(self):
        self.driver.find_element(By.XPATH, self.btnUserTab_xpath).click()

    def setMessage(self, messages):
        self.driver.find_element(By.XPATH, self.setSearch).clear()
        self.driver.find_element(By.XPATH, self.setSearch).send_keys(messages)

    def clickOnSendMessage(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
