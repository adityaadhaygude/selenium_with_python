import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#if your browser closes automatically then add below two lines and pass options to driver object
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("/home/aditya_dhaygude@acds.net.in/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(options=options, service=service_obj)

#wait for the webelements implicitely
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(1)
elements = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for element in elements:
    element.click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, '//div[@class="action-block"]/button').click()

#time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

#driver.find_element(By.TAG_NAME, "select").click()
select = Select(driver.find_element(By.TAG_NAME, "select"));
select.select_by_visible_text("India")

driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
driver.find_element(By.XPATH, "//div[@class='wrapperTwo']/button").click()
time.sleep(15)
#driver.close()