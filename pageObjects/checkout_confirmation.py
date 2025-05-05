from selenium.webdriver.common.by import By


class Checkout_Confirmation:

    def __int__(self, driver):





    def checkout(self):



    def enter_delivery_add(self):
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element(By.LINK_TEXT, "India").click()
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "[type=""submit]").click()



    def validate_order(self):
