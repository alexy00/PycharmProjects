from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class ContactUS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = ("http://lolivebleue.com")
        cls.driver.get(page_url)



    def test_a_contactSuccess(self): # Test # 1
        '''
        To verify contact result message when all required information is entered correctly'

        '''

        cont = self.driver.find_element(By.XPATH, ".//ul[@id='primary-parallax-menu']//a[text()='Contact']")
        cont.click()
        time.sleep(2)

        name = self.driver.find_element(By.NAME, "your-name")
        name.clear()
        name.send_keys("Al")
        time.sleep(2)

        email = self.driver.find_element(By.NAME, "your-email")
        email.clear()
        email.send_keys("alba@gmail.com")
        time.sleep(2)

        subj = self.driver.find_element(By.NAME, "your-subject")
        subj.clear()
        subj.send_keys("Olive is good!")
        time.sleep(2)

        phone = self.driver.find_element(By.NAME, "tel")
        phone.clear()
        phone.send_keys("3052222222")
        time.sleep(2)

        send= self.driver.find_element(By.XPATH, ".//input[@value='Send']")
        send.click()
        time.sleep(2)

        element = self.driver.find_element(By.XPATH,".//form[@class='wpcf7-form sent']//div[text()='Thank you for your message. It has been sent.']")
        output = element.text
        print("The message reads--> ", output)
        if element is not None:
            print("Contact submission is cuccessful")
        else:
            print("Contact submission failed")


    def test_b_contactAllBlank(self):  # Test # 2
        '''
        To verify error message under the 'Your Email" field when all fields are blank

        '''

        cont = self.driver.find_element(By.XPATH, ".//ul[@id='primary-parallax-menu']//a[text()='Contact']")
        cont.click()
        time.sleep(2)

        send= self.driver.find_element(By.XPATH, ".//input[@value='Send']")
        send.click()
        time.sleep(2)

        element = self.driver.find_element(By.XPATH,".//div[@id='wpcf7-f10843-o1']//span[text()='The e-mail address entered is invalid.']")
        output = element.text
        print("The error message reads--> ", output)
        if element is not None:
            print("The error message is displayed")
        else:
            print("The error message is not displayed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)
