from selenium.webdriver.support.select import Select

class Search():
    # Findtutor Page
    txtFind_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    txtFind_city_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/input"
    lnkFindtutor_menu_name = "Find tutor"
    lnkSearchCourse_menu_name="Search Course"
    lnkText_book_name = "Text Book"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"
    sltSyllabus="syllabus_id"
    sltClass="class_id"
    sltSubject="subject_id"
    sltMode="mode"
    sltgender="gender"
    txtExperience_xpath="//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[7]/input"
    btnGo_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[2]/div[4]/button"
    btnTextbookSearchGo_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div[2]/div[5]/button"
    txtSearchByBookName="//*[@id='BookName']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnFindTutorMenu(self):
        self.driver.find_element_by_link_text(self.lnkFindtutor_menu_name).click()

    def clickOnSearchCourseMenu(self):
        self.driver.find_element_by_link_text(self.lnkSearchCourse_menu_name).click()

    def clickOnTextBookMenu(self):
        self.driver.find_element_by_link_text(self.lnkText_book_name).click()

    def setSearchbox(self, search):
        self.driver.find_element_by_xpath(self.txtFind_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFind_xpath).send_keys(search)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def setSearchboxCity(self, search):
        self.driver.find_element_by_xpath(self.txtFind_city_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFind_city_xpath).send_keys(search)

    def drpSyllabus(self,search):
        select = Select(self.driver.find_element_by_name(self.sltSyllabus))
        select.select_by_visible_text(search)

    def drpClass(self,search):
        select = Select(self.driver.find_element_by_name(self.sltClass))
        select.select_by_visible_text(search)

    def drpSubject(self,search):
        select = Select(self.driver.find_element_by_name(self.sltSubject))
        select.select_by_visible_text(search)

    def drpMode(self,search):
        select = Select(self.driver.find_element_by_name(self.sltMode))
        select.select_by_visible_text(search)

    def drpGender(self,search):
        select = Select(self.driver.find_element_by_name(self.sltgender))
        select.select_by_visible_text(search)

    def setExperience(self, search):
        self.driver.find_element_by_xpath(self.txtExperience_xpath).clear()
        self.driver.find_element_by_xpath(self.txtExperience_xpath).send_keys(search)
    def clickg(self):
        self.driver.find_element_by_xpath(self.btnGo_xpath).click()

    def setSearchByBookName(self, search):
        self.driver.find_element_by_xpath(self.txtSearchByBookName).clear()
        self.driver.find_element_by_xpath(self.txtSearchByBookName).send_keys(search)

    def clickTextBookSearchGo(self):
        self.driver.find_element_by_xpath(self.btnTextbookSearchGo_xpath).click()
