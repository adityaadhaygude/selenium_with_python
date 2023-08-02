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

driver.get("https://www.sololearn.com/")

#give position to which need to scroll or use document.body.scrollHeight to go to the end of document.
driver.execute_script("window.scrollBy(0,500);")

driver.get_screenshot_as_file("1.png")