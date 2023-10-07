import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:
   

   @pytest.mark.tcid33
   def test_end_to_end_checkout_guest_user(self):

        home_page = HomePage(self.driver)
        header = Header(self.driver)

        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()
        header.click_right_cart_icon_header() 
        header.wait_until_cart_item_count(1) 
       
    # go to cart
    # apply free coupom
    # select free shipping 
    # clcick on checkout
    # verify order went through 