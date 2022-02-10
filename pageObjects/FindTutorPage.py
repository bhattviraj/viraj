from selenium.webdriver.support.select import Select


class FindTutor():
    # Findtutor Page
    txtFind_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/input"
    txtFind_city_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/input"
    lnkFindtutor_menu_name = "Find tutor"
    btnSearch_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/button"
    sltSyllabus="syllabus_id"
    sltClass="class_id"
    sltSubject="subject_id"
    sltMode="mode"
    sltgender="gender"
    txtExperience_xpath="//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[7]/input"
    btnGo_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[3]/div/div[8]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnFindTutorMenu(self):
        self.driver.find_element_by_link_text(self.lnkFindtutor_menu_name).click()

    def setSearchbox(self, findtutor):
        self.driver.find_element_by_xpath(self.txtFind_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFind_xpath).send_keys(findtutor)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def setSearchboxCity(self, findtutor):
        self.driver.find_element_by_xpath(self.txtFind_city_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFind_city_xpath).send_keys(findtutor)

    def drpSyllabus(self,findtutor):
        select = Select(self.driver.find_element_by_name(self.sltSyllabus))
        select.select_by_visible_text(findtutor)

    def drpClass(self,findtutor):
        select = Select(self.driver.find_element_by_name(self.sltClass))
        select.select_by_visible_text(findtutor)

    def drpSubject(self,findtutor):
        select = Select(self.driver.find_element_by_name(self.sltSubject))
        select.select_by_visible_text(findtutor)

    def drpMode(self,findtutor):
        select = Select(self.driver.find_element_by_name(self.sltMode))
        select.select_by_visible_text(findtutor)

    def drpGender(self,findtutor):
        select = Select(self.driver.find_element_by_name(self.sltgender))
        select.select_by_visible_text(findtutor)

    def setExperience(self, findtutor):
        self.driver.find_element_by_xpath(self.txtExperience_xpath).clear()
        self.driver.find_element_by_xpath(self.txtExperience_xpath).send_keys(findtutor)
    def clickg(self):
        self.driver.find_element_by_xpath(self.btnGo_xpath).click()
