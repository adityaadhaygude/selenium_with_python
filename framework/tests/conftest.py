import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#we can set command line option to accept browser using below custom code
def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome', help='Set browser'
    )


@pytest.fixture(scope="class")
def setup(request):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    #here extract browser name from the command line using request
    browser_name = request.config.getoption("browser_name")

    if browser_name == 'chrome':    
        service_obj = Service("/home/aditya_dhaygude@acds.net.in/Downloads/chromedriver_linux64/chromedriver")
        driver = webdriver.Chrome(options=options, service=service_obj)

    elif browser_name == 'firefox':
        print("---------FIREFOX--------")

    elif browser_name == 'IE':
        print("---------IE--------")
    
    #wait for the webelements implicitely
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
