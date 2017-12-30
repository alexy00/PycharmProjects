from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class Home(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = ("http://www.alliedhealthmedia.com/")
        cls.driver.get(page_url)
        print("The title of Home page is: ", cls.driver.title)
        print('page URL is: ', cls.driver.current_url)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_ContactSuccessful(self):
        self.driver.execute_script("window.scrollBy(0, 2100);")
        time.sleep(3)

        Your_Name = self.driver.find_element(By.NAME, "your-name")
        Your_Name.send_keys("alba")

        Email = self.driver.find_element(By.NAME, "your-email")
        Email.send_keys("alba@gmail.com")
        time.sleep(5)

        Send = self.driver.find_element(By.XPATH, ".//input[@value='Send']")
        Send.click()
        time.sleep(5)
        success_msg = self.driver.find_element(By.XPATH, ".//form[@class='wpcf7-form sent']/"
                                                      "/div[text()='Your message was sent successfully. Thanks.']")
        result = success_msg.is_displayed()
        assert result == True
        print("Message is displayed-> ", result)
        print("The message text is -> ", success_msg.text)


        '''
        name_error = ".//span[@class='wpcf7-form-control-wrap your-name']/
        /span[text()='Please fill the required field.']"
        
        email_error =".//span[@class='wpcf7-form-control-wrap your-email']/
        /span[text()='Please fill the required field.']"
        
        validation_alert=".//form[@class='wpcf7-form invalid']/
        /div[text()='Validation errors occurred. Please confirm the fields and submit it again.']"
        
        '''


if __name__ == '__main__':
    unittest.main(verbosity=2)
