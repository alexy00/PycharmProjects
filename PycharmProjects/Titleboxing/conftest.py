import pytest
from selenium import webdriver

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")

    if browser == 'firefox':
        baseURL = "https://www.titleboxing.com/"  # <-------- URL
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on FF")
    else:
        baseURL = "https://www.titleboxing.com/" #<------------URL
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on Chrome")
        try:     # TITLE BOXING SPECIFIC <------TO CLICK THE POP UP
            driver.find_element_by_css_selector(".fancybox-item.fancybox-close").click()
        except:
            pass

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

# Chrome browser will run as default.
    # If need to run Firefox ...test.py --browser firefox