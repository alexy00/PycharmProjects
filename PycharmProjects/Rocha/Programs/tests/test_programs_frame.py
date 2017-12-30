from Programs.page.programs_page import ProgramsPage
from Navs.header_navs import HeaderNavs
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProgramsTestsFrame(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp, ):
        self.pp = ProgramsPage(self.driver)
        self.nav = HeaderNavs(self.driver)

    def setUp(self):
        self.nav.programsTab()


    def test_BBJ_ReadmoreLink(self):
        self.pp.clickBjjReadMoreLink()
        result = self.pp.assertTitle()
        assert result == True
        print("Title verified--> ", result)


    def test_MmaReadmoreLink(self):
        self.pp.clickMmareadMoreLink()
        result = self.pp.assertTitle2()
        assert result == True
        print("Title verified--> ", result)


        #   py.test -s -v Programs\tests\test_programs_frame.py --html=htmlreport.html