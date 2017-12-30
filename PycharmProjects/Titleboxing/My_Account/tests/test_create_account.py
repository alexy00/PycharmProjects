from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class MyAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = ("https://www.titleboxing.com/")
        cls.driver.get(page_url)
        print("The title of Home page is: ", cls.driver.title)
        print('page URL is: ', cls.driver.current_url)
        # this is to close the popup
        try:
            cls.driver.find_element_by_css_selector(".fancybox-item.fancybox-close").click()
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    '''
    def test_CreateAccountPasswordErrorMsg(self):  # Pasword = 7 characters
        time.sleep(5)
        My_Account = self.driver.find_element(By.XPATH, "//a[@class='toolbar-btn toolbar-account icon-user']")
        My_Account.click()
        First_Name = self.driver.find_element(By.ID, "firstname")
        First_Name.send_keys("Al")
        Last_Name = self.driver.find_element(By.ID, "lastname")
        Last_Name.send_keys("Ba")
        Email = self.driver.find_element(By.ID, "email_address")
        Email.send_keys("alba@gmail.com")
        Password = self.driver.find_element(By.ID, "password")
        Password.send_keys("alba123")
        Password_confirmation = self.driver.find_element(By.ID, "confirmation")
        Password_confirmation.send_keys("alba123")
        Is_Subscribed = self.driver.find_element(By.ID, "is_subscribed")
        Is_Subscribed.click()
        time.sleep(2)
        Submit = self.driver.find_element(By.XPATH, ".//form[@id='form-validate']//button[@title='Submit']")
        Submit.click()
        print(self.driver.title)

        # Error message Varification
        Msg = self.driver.find_element(By.ID, "advice-validate-password-8-password")
        result = Msg.is_displayed()
        assert result == True
        print("Password validation message is displayed")
        print("The message text is---> ", Msg.text)


    def test_CreateAccountSuccessful(self):
        time.sleep(5)
        My_Account = self.driver.find_element(By.XPATH, "//a[@class='toolbar-btn toolbar-account icon-user']")
        My_Account.click()
        First_Name = self.driver.find_element(By.ID, "firstname")
        First_Name.send_keys("Al")
        Last_Name = self.driver.find_element(By.ID, "lastname")
        Last_Name.send_keys("Ba")
        Email = self.driver.find_element(By.ID, "email_address")
        Email.send_keys("alba@gmail.com")
        Password = self.driver.find_element(By.ID, "password")
        Password.send_keys("alba1234")
        Password_confirmation = self.driver.find_element(By.ID, "confirmation")
        Password_confirmation.send_keys("alba1234")
        Sign_email = self.driver.find_element(By.ID, "is_subscribed")
        Sign_email.click()
        time.sleep(5)
        Submit = self.driver.find_element(By.XPATH, ".//form[@id='form-validate']//button[@title='Submit']")
        Submit.click()

        element = self.driver.find_element(By.XPATH, "//div[@class='page-title']/h1[contains(text(),'Sign In or Create an Account')]")
        result = element.is_displayed()
        assert result == True
    '''
    def test_signInSiccessful(self):

        time.sleep(3)
        My_Account = self.driver.find_element(By.XPATH, "//a[@class='toolbar-btn toolbar-account icon-user']")
        My_Account.click()
        Email = self.driver.find_element(By.ID, "email")
        Email.send_keys("alba@gmail.com")
        Pass = self.driver.find_element(By.ID, "pass")
        Pass.send_keys("alba1234")
        Remember_Me = self.driver.find_element(By.CSS_SELECTOR, "[id*='remember_me']")
        Remember_Me.click()
        Sign = self.driver.find_element(By.ID, "send2")
        Sign.click()
        time.sleep(5)
        print(self.driver.title)
        element = self.driver.find_element(By.XPATH, "//div[@class='block-title']//span[text()='My Account']")
        result = element.is_displayed()
        assert result == True



if __name__ == '__main__':
    unittest.main(verbosity=2)