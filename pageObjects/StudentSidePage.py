import time

from selenium.webdriver.common.by import By


class student_side_flow:
    # Student Role

    lnkMoreItems_xpath = "//*[@id='root']/div/div[2]/div[1]/div/div[8]/div/button"
    lnkCourse_name = "Search Course"
    txtSearchCourse_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    btnSearchCourse_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"
    lnkMyCourses_name = "Courses"
    btnJoinNow_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div/div[3]/div/div[1]/button"
    btnConfirmJoinNow_xpath = "/html/body/div[2]/div/div[3]/button[1]"

    btnSubscribedCourses_xpath = "//*[@id='Completed']"
    btnCompletedCourses_xpath = "//*[@id='Completed']"
    btnInProgressCourses_xpath = "//*[@id='Uncompleted']"
    txtSearchMyCourse_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    btnSearchMyCourse_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"
    lnkCoursesMenu_name = "Course"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearchCourseMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkCourse_name).click()

    def setSearchCourse(self,course):
        self.driver.find_element(By.XPATH, self.txtSearchCourse_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchCourse_xpath).send_keys(course)
    def clickOnSearchCourse(self):
        self.driver.find_element(By.XPATH, self.btnSearchCourse_xpath).click()

    def clickOnInProgressCourses(self):
        self.driver.find_element(By.XPATH, self.btnInProgressCourses_xpath).click()

    def setSearchMyCourse(self, course):
        self.driver.find_element(By.XPATH, self.txtSearchMyCourse_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchMyCourse_xpath).send_keys(course)

    def clickOnSearchMyCourse(self):
        self.driver.find_element(By.XPATH, self.btnSearchMyCourse_xpath).click()

    def clickOnMoreItems(self):
        self.driver.find_element(By.XPATH, self.lnkMoreItems_xpath).click()

    def clickOnCoursesMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkCoursesMenu_name).click()

    def clickOnSubscribedCourses(self):
        self.driver.find_element(By.XPATH, self.btnSubscribedCourses_xpath).click()

    def clickOnInProgressCourses(self):
        self.driver.find_element(By.XPATH, self.btnInProgressCourses_xpath).click()

    def clickOnJoinNowCourse(self):
        self.driver.find_element(By.XPATH, self.btnJoinNow_xpath).click()
        self.driver.find_element(By.XPATH, self.btnConfirmJoinNow_xpath).click()
