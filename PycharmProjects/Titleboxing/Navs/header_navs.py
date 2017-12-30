import logging
from Base.selenium_driver import SeleniumDriver
import Utilities.custom_logger as cl


class NavigationPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    _pop_up = ".fancybox-item.fancybox-close"
    _gloves = "//a[@class='level-top']/span[text()='Gloves']"
    _protective = "//a[@class='level-top']/span[text()='Protective']"

    def clickPopUp(self):
        try:
            self.elementClick(self._pop_up, locatorType="css")

        except:
            pass



    def glovesTab(self):

        self.waitForElement(self._gloves, locatorType="xpath")
        self.elementClick(self._gloves, locatorType="xpath")

    
    def protective(self):
        self.elementClick(self._protective,locatorType="xpath")

    def protectiveTab(self):
        self.clickPopUp()
        self.protective()




