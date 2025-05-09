from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice/")
# //a[contains(@href, 'shop')]         a[href*='shop']    #two ways of using regular expression

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# my try
# products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]/div/h4/a')
#
# for phone in products:
#     print(phone.text)


products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

for product in products:
    product_Name = product.find_element(By.XPATH, "div/h4/a").text
    if product_Name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,  "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type=""submit]").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
print(successText)

# as the text is long enough we wont use == (we'll have to add the whole text . we'll use "in")
assert "Success! Thank you!" in successText
driver.close()