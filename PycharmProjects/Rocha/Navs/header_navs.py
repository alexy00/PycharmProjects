import logging
from Base.selenium_driver import SeleniumDriver
import Utilities.custom_logger as cl


class HeaderNavs(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    _home = ".//ul[@id='top-menu']//a[text()='Home']"
    _programs = ".//ul[@id='top-menu']//a[text()='Programs']"
    _about  = ".//ul[@id='top-menu']//a[text()='About']"
    _why_our_school = ".//ul[@id='top-menu']//a[text()='Why Our School']"
    _gallery = ".//ul[@id='top-menu']//a[text()='Gallery']"
    _news = ".//ul[@id='top-menu']//a[text()='News']"
    _contact = ".//ul[@id='top-menu']//a[text()='Contact']"

    def homeTab(self):
        self.elementClick(self._home,locatorType="xpath")
    
    def programsTab(self):
        self.elementClick(self._programs,locatorType="xpath")

    def aboutTab(self):
        self.elementClick(self._about,locatorType="xpath")

    def WhyOurSchoolTab(self):
        self.elementClick(self._why_our_school, locatorType="xpath")

    def GalleryTab(self):
        self.elementClick(self._gallery, locatorType="xpath")

    def NewsTab(self):
        self.elementClick(self._news, locatorType="xpath")

    def ContactTab(self):
        self.elementClick(self._contact, locatorType="xpath")


