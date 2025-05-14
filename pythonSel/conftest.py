import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",dest="myoption", default="chrome",help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    # options = Options()
    # options.add_argument('--ignore-certificate-errors')
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome": #firefox
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.implicitly_wait(4)
    yield driver #before test function execution
    # driver.close() #after test function execution
    # driver.quit()