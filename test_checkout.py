import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_to_cart_and_checkout(driver):
    # Search product
    driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
    time.sleep(5)

    # Get results
    results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
    count = len(results)

    # Assertion
    assert count > 0

    # Add all items to cart
    for result in results:
        result.find_element(By.XPATH, "div/button").click()

    # Go to cart
    driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
    driver.find_element(By.XPATH, "//button[.='PROCEED TO CHECKOUT']").click()
    time.sleep(2)

    # Apply promo code
    driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
    driver.find_element(By.XPATH, "//button[.='Apply']").click()
    time.sleep(5)

    # Scroll
    driver.execute_script("window.scrollBy(0,600)")

    # Place order
    driver.find_element(By.XPATH, "//button[.='Place Order']").click()
    time.sleep(3)

    # Select country
    ele = driver.find_element(By.XPATH, "//select[@style='width: 200px;']")
    dropdown = Select(ele)
    dropdown.select_by_visible_text("India")

    # Agree & Proceed
    driver.find_element(By.XPATH, "//input[@class='chkAgree']").click()
    driver.find_element(By.XPATH, "//button[.='Proceed']").click()
