from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Search():
    # Findtutor Page
    txtFind_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    txtFind_city_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/input"
    lnkFindtutor_menu_name = "Find tutor"
    lnkSearchCourse_menu_name = "Search Course"
    lnkText_book_name = "Textbook"
    lnkText_feedback_name = "Feedbacks"
    lnkText_QuestionAnswers_name = "Question & Answers"
    txt_search_feedback_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/input"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"
    btnSearchFeedback_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/button"
    btnQuestionAnswersSearchGo_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[3]/div[4]/button"
    sltSyllabus = "syllabus_id"
    sltClass = "class_id"
    sltSubject = "subject_id"
    sltMode = "mode"
    sltgender = "gender"
    txtExperience_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[7]/input"
    btnGo_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[2]/div[4]/button"
    btnTextbookSearchGo_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div[2]/div[5]/button"
    txtSearchByBookName = "//*[@id='BookName']"
    txtQusAnsSearchBox_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div[2]/input"
    btnQusAnsSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnFindTutorMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkFindtutor_menu_name).click()

    def clickOnSearchCourseMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkSearchCourse_menu_name).click()

    def clickOnQuestionAnswersMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkText_QuestionAnswers_name).click()

    def clickOnTextBookMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkText_book_name).click()

    def clickOnFeedbackMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkText_feedback_name).click()

    def setSearchFeedbackBox(self, search):
        self.driver.find_element(By.XPATH, self.txt_search_feedback_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_search_feedback_xpath).send_keys(search)

    def setSearchbox(self, search):
        self.driver.find_element(By.XPATH, self.txtFind_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFind_xpath).send_keys(search)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def clickFeedbackSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearchFeedback_xpath).click()

    def clickQuestionAnswersSearchGo(self):
        self.driver.find_element(By.XPATH, self.btnQuestionAnswersSearchGo_xpath).click()

    def setSearchboxCity(self, search):
        self.driver.find_element(By.XPATH, self.txtFind_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFind_city_xpath).send_keys(search)

    def drpSyllabus(self, search):
        select = Select(self.driver.find_element(By.NAME, self.sltSyllabus))
        select.select_by_visible_text(search)

    def drpClass(self, search):
        select = Select(self.driver.find_element(By.NAME, self.sltClass))
        select.select_by_visible_text(search)

    def drpSubject(self, search):
        select = Select(self.driver.find_element(By.NAME, self.sltSubject))
        select.select_by_visible_text(search)

    def drpMode(self, search):
        select = Select(self.driver.find_element(By.NAME, self.sltMode))
        select.select_by_visible_text(search)

    def drpGender(self, search):
        select = Select(self.driver.find_element(By.NAME, self.sltgender))
        select.select_by_visible_text(search)

    def setExperience(self, search):
        self.driver.find_element(By.XPATH, self.txtExperience_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtExperience_xpath).send_keys(search)

    def clickg(self):
        self.driver.find_element(By.XPATH, self.btnGo_xpath).click()

    def setSearchByBookName(self, search):
        self.driver.find_element(By.XPATH, self.txtSearchByBookName).clear()
        self.driver.find_element(By.XPATH, self.txtSearchByBookName).send_keys(search)

    def clickTextBookSearchGo(self):
        self.driver.find_element(By.XPATH, self.btnTextbookSearchGo_xpath).click()

    def setQusAnsSearchBox(self, search):
        self.driver.find_element(By.XPATH, self.txtQusAnsSearchBox_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtQusAnsSearchBox_xpath).send_keys(search)

    def clickOnQusAnsSearch(self):
        self.driver.find_element(By.XPATH, self.btnQusAnsSearch_xpath).click()
