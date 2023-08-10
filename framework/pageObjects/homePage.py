from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    searchBox = (By.CSS_SELECTOR, ".search-keyword")

    def homeItems(self):
        return self.driver.find_element(*HomePage.searchBox)