from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # collect all veggie names ->  BrowserSortedveggieList (A, B, C)
    veggieWebelements = driver.find_elements(By.XPATH, "//tr/td[1]")
    # print(veggieWebelements)

    for ele in veggieWebelements:
        browserSortedVeggies.append(ele.text)
    # print(browserSortedVeggies)  # print the unsorted list out

    ogBrowserSortedList = browserSortedVeggies.copy()
    # Sort this browserSortedVeggies -> newSortedList -> (A, B, C)
    browserSortedVeggies.sort()
    # print(browserSortedVeggies)

    assert browserSortedVeggies == ogBrowserSortedList

