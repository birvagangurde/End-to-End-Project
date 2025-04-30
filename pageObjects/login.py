from selenium.webdriver.common.by import By


class LoginPage:


    def __init__(self):
        self.username_input = (By.ID, "username")


    def login(self):
        driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
        driver.find_element(By.NAME, "password").send_keys("learning")
        driver.find_element(By.ID, "signInBtn").click()

