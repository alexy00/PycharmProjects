from My_Account.page.sign_page import SignPage
from Utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ContactTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = SignPage(self.driver)
        self.ts = TestStatus(self.driver)


    #@pytest.mark.run(order=1)
    def test_signInSuccessful(self):
        self.sp.signIn("alba@gmail.com","alba1234")
        result1 = self.sp.verifyTitle()
        self.ts.mark(result1, "title Verification")
        result2 = self.sp.verifySignInSuccessful()
        self.ts.markFinal("test_signInSuccessful",result2, "SignIn Successful")







        # py.test -s -v My_Account\tests\test_login_frame.py