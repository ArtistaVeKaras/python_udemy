import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid23
    def test_login_none_existing_user(self):
        
        my_account = MyAccountSignedOut(self)
        my_account.go_to_my_account()
        my_account.input_login_username('name')
        my_account.input_login_password('password')
        my_account.click_login_button()
        
        # error msg
        error_message = 'ERROR: Invalid username. Lost your password'
        my_account.wait_until_error_is_displayed(error_message)