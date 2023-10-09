from ssqatest.ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.ssqatest.src.pages.locators.CartPageLocators import CartLocator

class CartPage(CartLocator):
    
    def __init__(self,driver):
        self.driver = driver
        self.sl  = SeleniumExtended(self.driver)
 
    def go_to_cart_page(self):
         pass

      
    def get_all_products_in_cart(self): 
        """this function will get all the elements in the cart
        and will loop each product in the cart and get the text
        """

        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        return product_names
    
    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)
    
    def click_and_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)
        
    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_and_apply_coupon()

        success_msg = self.get_coupon_success_message()
        assert success_msg == 'Coupon code applied successfully.', f'Unexpected message when applying coupon'

        
    def get_coupon_success_message(self):
        text = self.sl.wait_and_get_text(self.CART_PAGE_MESSAGE)
        return text

    def click_proceed_to_checkout(self):
        self.sl.wait_and_click(self.CLICK_PROCEED_TO_CHECKOUT)
