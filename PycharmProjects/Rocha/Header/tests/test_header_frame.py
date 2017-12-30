from Header.page.header_page import HeaderPage
#from Utilities.teststatus import TestStatus
#from Navs.header_navs import HeaderNavs
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ContactTestsFrame(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HeaderPage(self.driver)



    def test_articleHeaderVerification(self):
        self.hp.articleHeader()

        result1 = self.hp.assertTitle()
        assert result1 == True
        print("Title verified--> ",result1)


        result2 = self.hp.assertArticleHeaderDisplayed()
        assert result2== True
        print("Article header is  displayed--> ",result2)
        self.hp.logArticleHeaderText()  # To log Captcha text



     # py.test -s -v Header\tests\test_header_frame.py
