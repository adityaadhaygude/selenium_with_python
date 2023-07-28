import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH, "//div[@class='example']/a").click()

#below two lines will store the windows opened in the order and switch to the last used window
windows_list = driver.window_handles
driver.switch_to.window(windows_list[-1])

print(driver.find_element(By.TAG_NAME, "h3").text)
