from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    
    
    BILLING_FIRST_NAME = (By.ID, 'billing_first_name')
    BILLING_LAST_NAME = (By.ID, 'billing_last_name')
    BILLING_COUNTRY_REGION = (By.ID, 'select2-billing_country-container')
    BILLING_STREET_ADDRESS = (By.ID, 'billing_address_1')
    BILLING_TOWN_CITY = (By.ID, 'billing_city')
    BILLING_POST_CODE = (By.ID, 'billing_postcode')
    BILLING_PHONE_NUMBER = (By.ID, 'billing_phone')
    BILLING_EMAIL_ADDRESS = (By.ID, 'billing_email')
    BILLING_PLACE_ORDER_BTN = (By.ID, 'billing_email')
    PLACE_ODER_BTN = (By.ID, 'place_order')