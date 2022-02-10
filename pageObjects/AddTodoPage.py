import time
from selenium.webdriver.support.ui import Select

class AddTodo:
    # Add TodoTask
    lnkTodo_menu_name = "To do"
    txtTask_name = "name"
    btnAddTodo_xpath = "//button[@type='submit']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnTodoMenu(self):
        self.driver.find_element_by_link_text(self.lnkTodo_menu_name).click()

    def setTodo(self,task):
        self.driver.find_element_by_name(self.txtTask_name).clear()
        self.driver.find_element_by_name(self.txtTask_name).send_keys(task)

    def clickOnAddTodo(self):
        self.driver.find_element_by_xpath(self.btnAddTodo_xpath).click()