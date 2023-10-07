import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os


@pytest.fixture(scope="class")
def init_driver(request):
    global driver
    supported_browsers = ['chrome', 'ch' 'headlesschrome', 'headlessfirefox','firefox', 'ff']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("the environment variable 'BROWSER' must be specified.")
   
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not supported."
                        f"Supported browsers are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options) # export BROSWER=headlesschrome set the browser in the terminal by running the following command
        
    elif browser in ('headlessfirefox'):
        ff_options = FFOptions()
        ff_options.add_argument('--disable-gpu')
        ff_options.add_argument('--no-sandbox')
        ff_options.add_argument('headless')
        driver = webdriver.Firefox(options=ff_options)  # export BROSWER=headlesschrome
        

    request.cls.driver = driver
    yield
    driver.quit()
 

