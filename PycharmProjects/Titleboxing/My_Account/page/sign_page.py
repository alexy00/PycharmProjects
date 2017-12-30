import logging
from Base.basepage import BasePage
import Utilities.custom_logger as cl


class SignPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    ### Locators ###
    _pop_up = ".fancybox-item.fancybox-close"
    _my_account = "//a[@class='toolbar-btn toolbar-account icon-user']"
    _email = "email"
    _password = "pass"
    _remember_me = "[id*='remember_me']"
    _sign_button = "send2"
    _verify_element = "//div[@class='block-title']//span[text()='My Account']"

    ### Element Interactions ###

    def clickPopUp(self):
        popUp = self.elementClick(self._pop_up, locatorType="css")
        if popUp is None:
            pass

    def clickOnMyAccount(self):
        self.elementClick(self._my_account, locatorType="xpath")

    # SCROLL UP#


    def enterEmail(self, email):
        self.sendKeys(email, self._email)

    def enterPassword(self, password):
        self.sendKeys(password, self._password)

    def clickOnRememberMe(self):
        self.elementClick(self._remember_me, locatorType="css")

    def clickOnSign(self):
        self.elementClick(self._sign_button)


    def signIn(self,email="",password=""):
        self.clickPopUp()
        self.waitForElement(self._my_account,"xpath")
        self.clickOnMyAccount()
        self.webScroll(direction="up")
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickOnRememberMe()
        self.clickOnSign()
        self.sleep(sec=3)



    def verifySignInSuccessful(self):
        result = self.isElementPresent(".block-title>strong>span",
                                         locatorType="css")
        return result

    def verifyTitle(self):      # <--From Base Page
        return self.verifyPageTitle("My Account - TITLE Boxing")


    '''    
        if "Sign In or Create an Account" in self.getTitle():
            return True
        else:
            return False
    '''





