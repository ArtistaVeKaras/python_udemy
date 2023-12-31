from selenium.webdriver.common.by import By


class MyAccountSignedOutLocator:
    
    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[value="Log in"]')
    ERROR_UI = (By.CSS_SELECTOR, 'ul.woocommerce-error')

    REGISTER_EMAIL = (By.CSS_SELECTOR, 'reg_emial')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')