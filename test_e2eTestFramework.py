

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ShopPage import ShopPage
from pageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    shop_page = loginPage.login()
    shop_page.add_product_to_cart("Blackberry")
    shop_page.goToCart()

    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(successText)

    assert "Success! Thank you!" in successText
    driver.close()