from selenium.webdriver.common.by import By


class Network:
    # Network
    lnkNetwork_name = "Network"
    btnAdd_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/button"

    btnSubmit_xpath = "/html/body/div[2]/div/div/div[2]/form/div[12]/div/div[1]/button"

    txtSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"

    txtNewSearchFriend_xpath = "/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/div/input"
    btnAddSearchFriend_xpath = "/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[5]/div/button"
    btnConfirm_xpath = "/html/body/div[6]/div/div[3]/button[1]"

    btnInviteOption_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/button[6]"
    txtInviteEmail_xpath = "//*[@id='email']"
    btnInvite_xpath = "/html/body/div[2]/div/div/div[2]/form/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnNetworkMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkNetwork_name).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAdd_xpath).click()

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()

    def setSearchNetwork(self, network):
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(network)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def setNewSearchFriend(self, network):
        self.driver.find_element(By.XPATH, self.txtNewSearchFriend_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtNewSearchFriend_xpath).send_keys(network)

    def clickOnAddSearchFriend(self):
        self.driver.find_element(By.XPATH, self.btnAddSearchFriend_xpath).click()
        self.driver.find_element(By.XPATH, self.btnConfirm_xpath).click()

    def clickOnInviteOption(self):
        self.driver.find_element(By.XPATH, self.btnInviteOption_xpath).click()

    def setInviteEmail(self, network):
        self.driver.find_element(By.XPATH, self.txtInviteEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtInviteEmail_xpath).send_keys(network)

    def clickOnInvite(self):
        self.driver.find_element(By.XPATH, self.btnInvite_xpath).click()
