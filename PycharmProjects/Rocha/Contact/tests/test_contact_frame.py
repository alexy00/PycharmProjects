from Contact.page.contact_page import ContactPage
#from Utilities.teststatus import TestStatus
from Navs.header_navs import HeaderNavs
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ContactTestsFrame(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.cp = ContactPage(self.driver)
        #self.ts = TestStatus(self.driver)
        self.nav = HeaderNavs(self.driver)

    def setUp(self):
        self.nav.ContactTab()



    def test_Contact(self):

        self.cp.contact("Al","Ba","ab@gmail.com","111 111 1111","LA","California",
                        "22002","none")

        result1 = self.cp.assertTitle()
        assert result1 == True
        print("Title verified--> ",result1)


        result2 = self.cp.assertCaptchaValidationMsgDisplayed()
        assert result2== True
        print("Captcha validation message displayed--> ",result2)
        self.cp.logCaptchaText()  # To log Captcha text



     # py.test -s -v Contact\tests\test_contact_frame.py






