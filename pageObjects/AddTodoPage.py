import time
from selenium.webdriver.support.ui import Select


class AddTodo:
    # Add TodoTask
    lnkTodo_menu_name = "To do"
    txtTask_name = "name"
    btnAddTodo_xpath = "//button[@type='submit']"
    btnDeleteTodo_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[4]/div/div/div[3]/button"
    btnConfrmDeleteTodo_xpath = "/html/body/div[2]/div/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTodoMenu(self):
        self.driver.find_element_by_link_text(self.lnkTodo_menu_name).click()

    def setTodo(self, task):
        self.driver.find_element_by_name(self.txtTask_name).clear()
        self.driver.find_element_by_name(self.txtTask_name).send_keys(task)

    def clickOnAddTodo(self):
        self.driver.find_element_by_xpath(self.btnAddTodo_xpath).click()

    def clickOnDelete(self):
        self.driver.find_element_by_xpath(self.btnDeleteTodo_xpath).click()
        self.driver.find_element_by_xpath(self.btnConfrmDeleteTodo_xpath).click()
