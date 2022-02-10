import time
from selenium import webdriver
from utilities import XLUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:\Viraj\chromedriver_win32\chromedriver.exe")

driver.get("http://tutorpark.ssavts.in/#/")
driver.maximize_window()

path = r"D:\Documents\Downloads\tutorpark_signup.xlsx"
rows = XLUtils.getRowCount(path, "signup")
driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div/div/div/div/a/div/button").click()
time.sleep(2)
print(rows)
for r in range(2, rows + 1):
    print(r)
    first_name = XLUtils.readData(path, "signup", r, 1)
    last_name = XLUtils.readData(path, "signup", r, 2)
    email = XLUtils.readData(path, "signup", r, 3)
    phone = XLUtils.readData(path, "signup", r, 4)
    aadhar_id = XLUtils.readData(path, "signup", r, 5)
    password = XLUtils.readData(path, "signup", r, 6)
    password_confirmation = XLUtils.readData(path, "signup", r, 7)
    address = XLUtils.readData(path, "signup", r, 8)
    state_drp = XLUtils.readData(path, "signup", r, 9)
    city_drp = XLUtils.readData(path, "signup", r, 10)
    pincode = XLUtils.readData(path, "signup", r, 11)

    driver.find_element_by_name("first_name").send_keys(first_name)
    driver.find_element_by_name("last_name").send_keys(last_name)
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("phone").send_keys(phone)
    driver.find_element_by_name("aadhar_id").send_keys(aadhar_id)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password_confirmation").send_keys(password_confirmation)
    driver.find_element_by_name("address").send_keys(address)

    # Select State Dropdown code
    drpstate = driver.find_element(By.XPATH,
                                   "//div[@id='root']/div/div/div/div/div/div[2]/div/form/div[9]/div/div/div/div/input")
    driver.execute_script("arguments[0].click();", drpstate)
    # select From Auto Suggestion value
    drpstate.send_keys(state_drp)
    drpstate.send_keys(Keys.ARROW_DOWN)
    drpstate.send_keys(Keys.ENTER)

    drpcity = driver.find_element(By.XPATH,
                                  "//div[@id='root']/div/div/div/div/div/div[2]/div/form/div[9]/div[2]/div/div/div/input")
    driver.execute_script("arguments[0].click();", drpcity)
    drpcity.send_keys(city_drp)
    drpcity.send_keys(Keys.ARROW_DOWN)
    drpcity.send_keys(Keys.ENTER)

    driver.find_element_by_name("pincode").send_keys(pincode)
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div[2]/div/form/div[11]/div/div/button").click()
    time.sleep(4)
    if driver.current_url == "http://tutorpark.ssavts.in/#/register-successs":
        print("test id Passed")
        driver.get("http://tutorpark.ssavts.in/#/register")
        XLUtils.writeData(path, "signup", r, 12, "Test Passed Register Successfully")
    else:
        print("test is Failed")
        XLUtils.writeData(path, "signup", r, 12, "Test Failed Register Successfully")
        driver.get("http://tutorpark.ssavts.in/#/")

driver.get("http://tutorpark.ssavts.in/#/")