import pytest
from selenium import webdriver

#conftest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        s = Service(r"E:\Viraj\chromedriver_win32\chromedriver.exe")
        driver=webdriver.Chrome(service=s,options=options)
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'TutorPark'
    config._metadata['Module Name'] = 'Tutorpark'
    config._metadata['Tester'] = 'Viraj'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
