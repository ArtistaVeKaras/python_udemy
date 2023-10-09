from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.ssqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from ssqatest.ssqatest.src.helpers.generic_helpers import generate_random_email_and_password

class CheckoutPage(CheckoutPageLocators):
    
    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

         
    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name is None else "TestAutomation"
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME, 'Akiira_test')

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name is None else "Last Name"
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME, 'surname_test')
  
    def input_billing_country_region(self, country_region=None):
        pass

    def input_billing_street_add(self, address=None):
        address = address if address is None else "TestAutomation"
        self.sl.wait_and_input_text(self.BILLING_STREET_ADDRESS, '1 Bond Street')
    
    def input_billing_town_city(self, city=None):
        city = 'San Franscisco' if not city else city
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME, 'Nottingham')
     
    def input_billing_post_code(self, post_code=None):
        post_code = 'SED4 4TG' if post_code is None else post_code
        self.sl.wait_and_input_text(self.BILLING_STREET_ADDRESS, '1 Bond Street')
     
    def input_billing_phone_numer(self, phone=None):
        phone = '089098787798' if phone is None else phone
        self.sl.wait_and_input_text(self.BILLING_PHONE_NUMBER, '+440999999')
     
    def input_billing_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_ADDRESS, email)

    def fill_in_billing_info(self, f_name, l_name, country_region, address, city, postal_code, phone, email):
        self.input_billing_first_name(first_name = f_name)
        self.input_billing_last_name(last_name = l_name)
        self.input_billing_country_region(country_region = country_region)
        self.input_billing_street_add(address = address)
        self.input_billing_town_city(city = city)
        self.input_billing_post_code(post_code = postal_code)
        self.input_billing_phone_numer(phone = phone)
        self.input_billing_email(email = email)

    def place_order(self):
        self.sl.wait_and_click(self.PLACE_ODER_BTN)