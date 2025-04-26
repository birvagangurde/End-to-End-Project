import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browserInstance(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
