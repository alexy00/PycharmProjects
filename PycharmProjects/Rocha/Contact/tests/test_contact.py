from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest

class ContactPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = ("https://www.vagnerrochamartialarts.com/contact")
        cls.driver.get(page_url)
        print("The title of Contact page is: ", cls.driver.title)
        print('Page URL is: ', cls.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def test_State_select(self):
        
        Dropdown = self.driver.find_element(By.ID, "input_7_5_4")
        Select(Dropdown).select_by_visible_text("California")
        time.sleep(2)
        DropDownOption = self.driver.find_element(By.XPATH, ".//*[@id='input_7_5_4']//option[@value='California']")
        print("Is California selected?-> ", DropDownOption.is_selected())#TRUE/FALSE
        if DropDownOption.is_selected()== False:
            print("test_State_Select = FAIL")
            self.driver.get_screenshot_as_file("State_select.png")
            print("See piucture: State_select")


    def test_BJJ_checkbobox_click(self):

        self.driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(3)
        bjj_checkBox = self.driver.find_element(By.ID, "choice_7_6_1")
        bjj_checkBox.click()
        '''
        result = bjj_checkBox.is_selected()
        assert result == True
        '''
        print("BJJ box is selected--> ", bjj_checkBox.is_selected())
        if bjj_checkBox.is_selected()==False:
            print("test_BJJ_checkbox_click = FAIL")
            self.driver.get_screenshot_as_file("BJJ_check.png")
            print("See piucture: BJJ_check")
    
    def test_Captcha_error_msg_verification(self):
        submit = self.driver.find_element(By.ID, "gform_submit_button_7")
        submit.click()
        validation_msg = self.driver.find_element(By.XPATH,".//*[@id='field_7_4']//div[@class='gfield_description validation_message']")
        if validation_msg is not None:
            print("The Captcha validation Error message is presnt")
            print("The Captcha validation Error message--> ", validation_msg.text)
        else:
            print("The Captcha validation Error message is NOT present")
            print("test_Capcha_error_msg_verification = FAIL")
            self.driver.get_screenshot_as_file("Captha_msg.png")
            print("See piucture: Captcha_msg")
        



if __name__ == '__main__':
    unittest.main(verbosity=2)