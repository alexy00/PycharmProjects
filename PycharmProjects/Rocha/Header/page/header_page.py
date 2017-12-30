import logging
from Base.selenium_driver import SeleniumDriver
import Utilities.custom_logger as cl


class HeaderPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    _programs_tab = ".//ul[@id='top-menu']//a[text()='Programs']"  # from header tab
    _seminars = ".//ul[@id='top-menu']//a[text()='Seminars']"
    _article_header =".//article[@id='post-97']//h1[text()='MARTIAL ARTS & SELF DEFENSE SEMINARS']"


    def hoverPrograms(self):
        self.hoverOnElement(self._programs_tab,locatorType="xpath")

    def clickSeminars(self):
        self.hoverAndClick(self._seminars, locatorType="xpath")

    def clickArticleHeader(self):
        self.elementClick(self._article_header,locatorType="xpath")

    def articleHeader(self):
        self.hoverPrograms()
        self.clickSeminars()


    def assertArticleHeaderDisplayed(self):
        result = self.isElementDisplayed(self._article_header, locatorType="xpath")
        return result


    def logArticleHeaderText(self):
        result = self.logText(self._article_header, locatorType="xpath")
        return result




    def assertTitle(self):
        if "Martial Arts and Self Defense Seminars" in self.getTitle():
            return True
        else:
            return False






