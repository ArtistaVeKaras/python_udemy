import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers import generate_random_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tci13
    def test_register_valid_user(self):
       my_account_new_user = MyAccountSignedOut(self.driver)
       my_account_new_user.go_to_my_account()
       my_aacount_i = MyAccountSignedIn(self.driver)

       rand_email = generate_random_email_and_password()
       my_account_new_user.input_register_email(rand_email['email'])
       my_account_new_user.input_register_password('adfadsf3344')
       my_account_new_user.click_register_btn()

       my_aacount_i.verify_user_is_signed_in() 