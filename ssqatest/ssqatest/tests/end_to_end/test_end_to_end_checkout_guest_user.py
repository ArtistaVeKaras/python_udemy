import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.configs.generic_configs import GenericConfig
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.OrderReceivedPage import OrderReceivedPage
from ssqatest.src.helpers.database_helpers import get_order_from_db_by_order_no

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:
   

   @pytest.mark.tcid33
   def test_end_to_end_checkout_guest_user(self):

        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        order_page = OrderReceivedPage(self.driver)
        
        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()
        header.click_right_cart_icon_header() 
        header.wait_until_cart_item_count(1) 
        product_name = cart_page.get_all_products_in_cart() 
        assert len(product_name) == 1, f"Expected 1 item in cart but found {len(product_name)}"
        # apply free coupom

        coupon_code = GenericConfig.FREE_COUPON
        cart_page.apply_coupon(coupon_code)
        cart_page.get_coupon_success_message()
        cart_page.click_proceed_to_checkout()
        checkout_page.fill_in_billing_info('akira','bonds','L.A', 'Bond Street', 'London', 'SE23TG', '00987897','test@gmail.com')
        checkout_page.place_order()
        
        
        # verify order went through 
        order_page_header = 'Order received'
        order_txt = order_page.verify_order_received_page_locator(order_page_header)
        assert order_page_header == order_txt
        
        # verify order is recorded in db(via SQL or API)
        order_no = get_order_from_db_by_order_no(1)
        print(order_no)

        db_order = get_order_from_db_by_order_no(order_no)
        assert db_order, f"Afert creating order with FE, not foun in DB." \
                         f"Order no: {order_no}"