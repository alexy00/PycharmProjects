import logging
from Base.selenium_driver import SeleniumDriver
import Utilities.custom_logger as cl


class ContactPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    _contact_tab = ".//ul[@id='top-menu']//a[text()='Contact']"  # from header tab
    _contact_link = ".//*[@id='menu-item-4435']/a" # from footer link(need to scroll down)
    _first_name = "input_7_1_3"
    _last_name = "input_7_1_6"
    _email = "input_7_2"
    _phone = "input_7_3"
    _adress_city = "input_7_5_3"
    _adress_state = "input_7_5_4"
    _adress_zip = "input_7_5_5"  #(scroll down  800)
    _questions_comments = "input_7_7"
        # Interested in:
    _bjj = "choice_7_6_1"
    _kickboxing = "choice_7_6_2"
    _kids_martial_arts = "choice_7_6_3"
    _women_fitness_classes = "choice_7_6_4"
    _family_deals = "choice_7_6_5"
    _self_defense = "choice_7_6_6"
    _weight_loss = "choice_7_6_7"
    _submit_button = "gform_submit_button_7"

    def clickContactTab(self):
        self.elementClick(self._contact_tab, locatorType="xpath")

    def enterFirstName(self,name):
        self.sendKeys(name,self._first_name)

    def enterLastName(self,lastname):
        self.sendKeys(lastname,self._last_name)

    def enterEmail(self,email):
         self.sendKeys(email, self._email)

    def enterPhone(self,phone):
        self.sendKeys(phone, self._phone)

    def enterCity(self,city):
        self.sendKeys(city,self._adress_city)

    def selectState(self,state):
        self.selectByVisibleText(state,self._adress_state)

    def enterZipCode(self,zipcode):
        self.sendKeys(zipcode,self._adress_zip)

    def scrollDown(self):
        self.webScroll("down")

    def enterComments(self, comment):
        self.sendKeys(comment,self._questions_comments)

    #Interested In

    def checkBJJ(self):
        self.elementClick(self._bjj)

    def clickSubmit(self):
        self.elementClick(self._submit_button)

    def contact(self,name="",lastname="",email="",phone="",city="",state="",zipcode="",comments="",):
        #self.clickContactTab()
        self.enterFirstName(name)
        self.enterLastName(lastname)
        self.enterEmail(email)
        self.enterPhone(phone)
        self.enterCity(city)
        self.selectState(state)
        self.enterZipCode(zipcode)
        self.scrollDown()
        self.enterComments(comments)
        self.checkBJJ()
        self.clickSubmit()

    def assertCaptchaValidationMsgDisplayed(self):
        result = self.isElementDisplayed(".//li[@id='field_7_4']//div[@class='gfield_description validation_message']",
                                         locatorType="xpath")
        return result


    def logCaptchaText(self):
        result = self.logText(".//li[@id='field_7_4']//div[@class='gfield_description validation_message']",
                               locatorType="xpath")

        return result




    def assertTitle(self):
        if "Contact" in self.getTitle():
            return True
        else:
            return False














