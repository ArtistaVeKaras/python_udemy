from ssqatest.ssqatest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from ssqatest.ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging as logger

class MyAccountSignedOut(MyAccountSignedOutLocator):
   
    endpoint = '/my-account' 

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        
    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info("Going to my account: {my_account_url}") 
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)
        
    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.debug('Clicking the signing button!')
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_error):
        logger.info('Waiting for error msg to be displayed!')
        self.sl.wait_until_element_contains_text(self.ERROR_UI, exp_error)

    def input_register_email(self, reg_email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, reg_email)

    def input_register_password(self, reg_password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, reg_password)

    def click_register_btn(self):
        logger.debug('Clicking the signing button!')
        self.sl.wait_and_click(self.REGISTER_BTN)