from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/aditya_dhaygude@acds.net.in/Downloads/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
try:
    assert(driver.current_url == "https://www.google.com/")
    print("Test Passed...!")
except Exception as e:
    print(e)
    print("Test failed")
driver.close()