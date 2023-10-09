from selenium.webdriver.common.by import By

class CartLocator():
    
    
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item', 'tr.product-name')
    COUPON_FIELD = (By.ID, 'coupon_code')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, "button[name='apply_coupon']")

    
    CART_PAGE_MESSAGE = (By.CSS_SELECTOR, 'div.woocommerce-message')
    CLICK_PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, 'a.checkout-button')