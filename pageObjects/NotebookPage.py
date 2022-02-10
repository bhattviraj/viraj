class notebook:
    # Notebook
    lnkNotebook_name = "Notebook"
    lnkMoreItems_xpath="//*[@id='root']/div/div[2]/div[1]/div[2]/div[8]/div/button/div/div"
    txtSearch_xpath="//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div[2]/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMoreItems(self):
        self.driver.find_element_by_link_text(self.lnkMoreItems_xpath).click()

    def clickOnNotebookMenu(self):
        self.driver.find_element_by_link_text(self.lnkNotebook_name).click()

    def setSearchNotebook(self, notebook):
        self.driver.find_element_by_xpath(self.txtSearch_xpath).clear()
        self.driver.find_element_by_xpath(self.txtSearch_xpath).send_keys(notebook)

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()
