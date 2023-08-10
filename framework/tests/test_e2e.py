import pytest, time, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.homePage import HomePage
from utilities.BaseClass import Common 

class TestE2E(Common):
    def test_e2e(self):
        HomePageObj = HomePage(self.driver)
        HomePageObj.homeItems().send_keys("ber")
        time.sleep(1)
        elements = self.driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
        for element in elements:
            element.click()

        self.driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
        self.driver.find_element(By.XPATH, '//div[@class="action-block"]/button').click()

        #time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

        #driver.find_element(By.TAG_NAME, "select").click()
        select = Select(self.driver.find_element(By.TAG_NAME, "select"));
        select.select_by_visible_text("India")

        self.driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
        self.driver.find_element(By.XPATH, "//div[@class='wrapperTwo']/button").click()