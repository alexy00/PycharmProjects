from Gloves.page.gloves_page import GlovesPage
from Utilities.teststatus import TestStatus
from Navs.header_navs import NavigationPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class GlovesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.gp = GlovesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.glovesTab()

    @pytest.mark.run(order=1)
    def test_GlovesLink(self):
        self.gp.clickTrainingSparringGloves()
        result1 = self.gp.verifyTitle1()
        self.ts.mark(result1, "title Verification")
        result2 = self.gp.verifyTrainingSparringGlovesLink()
        self.ts.markFinal("test_GlovesLink", result2, "Link Successful")

    @pytest.mark.run(order=2)
    def test_BagGlovesLink(self):
        self.gp.clickBagGloves()
        result1 = self.gp.verifyTitle2()
        self.ts.mark(result1, "title Verification")
        result2 = self.gp.verifyBagGlovesLink()
        self.ts.markFinal("test_BagGlovesLink", result2, "Link Successful")

    @pytest.mark.run(order=3)
    def test_CompGlovesLink(self):
            self.gp.clickBagGloves()
            result1 = self.gp.verifyTitle3()
            self.ts.mark(result1, "title Verification")
            result2 = self.gp.verifyBagGlovesLink()
            self.ts.markFinal("test_CompGlovesLink", result2, "Link Successful")



        # py.test -s -v Gloves\tests\test_gloves_frame.py
