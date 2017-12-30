import Utilities.custom_logger as cl
import logging
from Base.basepage import BasePage

class GlovesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ### Locators ###

    _training_sparring = ".//dl[@id='narrow-by-list']//a[text()='Boxing Training / Sparring Gloves']"
    _bag_gloves = ".//dl[@id='narrow-by-list']//a[text()='Boxing Bag Gloves']"
    _comp_gloves = ".//dl[@id='narrow-by-list']//a[text()='Boxing Competition Gloves']"
    _fitness_gloves = ".//dl[@id='narrow-by-list']//a[text()='Fitness Boxing Gloves']"
    _mma_gloves = ".//dl[@id='narrow-by-list']//a[text()='MMA Training / Sparring Gloves']"
    _mma_bag = ".//dl[@id='narrow-by-list']//a[text()='MMA Bag Gloves']"
    _mma_competition = ".//dl[@id='narrow-by-list']//a[text()='MMA Competition Gloves']"

    ## Elements to verify

    _gloves_training = ".//div[@class='currently']//span[contains(text(),'Boxing Training / Sparring Gloves')]"
    _gloves_bag = ".//div[@class='currently']//span[contains(text(),'Boxing Bag Gloves')]"
    _gloves_comp = ".//div[@class='currently']//span[contains(text(),'Boxing Competition Gloves')]"
    ### Element Interactions ###
#-----------------------TEST 1--------------------------------------------------
    def clickTrainingSparringGloves(self):
        self.elementClick(self._training_sparring,locatorType="xpath")
        self.sleep(3)

    def verifyTitle1(self):      # <--From Base Page
        return self.verifyPageTitle("Boxing Gloves")

    def verifyTrainingSparringGlovesLink(self):
        self.waitForElement(self._gloves_training, locatorType="xpath")
        result = self.isElementPresent(self._gloves_training, "xpath")
        return result
# ---------------TEST 2-------------------------------------------------------

    def clickBagGloves(self):
        self.elementClick(self._bag_gloves,locatorType="xpath")
        self.sleep(3)

    def verifyTitle2(self):      # <--From Base Page
        return self.verifyPageTitle("Boxing Gloves")

    def verifyBagGlovesLink(self):
        self.waitForElement(self._gloves_bag, locatorType="xpath")
        result = self.isElementPresent(self._gloves_bag, "xpath")
        return result

#-----------------TEST 3 -----------------------------------------------------------

    def clicCompGloves(self):
        self.elementClick(self._comp_gloves, locatorType="xpath")
        self.sleep(3)

    def verifyTitle3(self):  # <--From Base Page
        return self.verifyPageTitle("Boxing Gloves")

    def verifyCompGlovesLink(self):
        self.waitForElement(self._gloves_bag, locatorType="xpath")
        result = self.isElementPresent(self._gloves_comp, "xpath")
        return result