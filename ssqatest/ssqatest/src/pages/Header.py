from ssqatest.ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.ssqatest.src.pages.locators.HeaderLocators import HeaderLocator

class Header(HeaderLocator):
    
    def __init__(self,driver):
        self.driver = driver 
        self.sl = SeleniumExtended(self.driver)

    def click_right_cart_icon_header(self):
        self.sl.wait_and_click(self.CART_RIGH_HEADER)

    def wait_until_cart_item_count(self, count):
        expected_count = str(count) + 'item'
        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_count)