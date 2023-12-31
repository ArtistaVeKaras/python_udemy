from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

import time


class SeleniumExtended:
    
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10
        
    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
            )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_and_get_text(self, locator, timeout=None):
        """ Waits for a locator to contain a text
        and returns the value of the locator

        Args:
            locator (_type_): _description_
            timeout (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: retunrn a string value
        """
        timeout = timeout if timeout else self.default_timeout

        ele = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
        element_text = ele.text()
    
        return element_text
    
    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"/unable to find element located by '{locator}' " \
                              f"after timeout '{timeout}"

        try:
            
           elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located (locator)
        )

        except TimeoutException:
            raise TimeoutException()
        
        return elements 