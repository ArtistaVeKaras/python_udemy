from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.ssqatest.src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

        
    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)
        
    def go_to_cart(self):
        pass

    def apply_free_coupoms(self):
        pass
    
    def select_free_shipping(self):
        pass
    
    def click_checkout_btn(self):
        pass
    
    def verify_order_validation(self):
        pass