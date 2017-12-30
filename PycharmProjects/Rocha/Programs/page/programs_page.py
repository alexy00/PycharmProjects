import logging
from Base.selenium_driver import SeleniumDriver
import Utilities.custom_logger as cl


class ProgramsPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    _programs = ".//ul[@id='top-menu']//a[text()='Programs']"
    _adultsBjj_readmore = ".//a[@title='Brazilian Jiu-Jistu' and contains(text(),'Read More')]"
    _mma_readmore = ".//a[@title='Mixed Martial Arts' and contains (text(), 'Read More')]"

    def programsTab(self):
        self.elementClick(self._programs,locatorType="xpath")

    def clickBjjReadMoreLink(self):
        self.elementClick(self._adultsBjj_readmore,locatorType="xpath")


    def assertTitle(self):
        if "Brazilian Jiu Jitsu Classes" in self.getTitle():
            return True
        else:
            return False


    def clickMmareadMoreLink(self):
        self.elementClick(self._mma_readmore,locatorType="xpath")



    def assertTitle2(self):
        if "Mixed Martial Arts" in self.getTitle():
            return True
        else:
            return False
