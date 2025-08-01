import os
import sys

from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page
