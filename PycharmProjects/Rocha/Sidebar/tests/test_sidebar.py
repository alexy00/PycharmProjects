from selenium import webdriver
from selenium.webdriver.common.by import By



import unittest

class Sidebar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.driver.get("https://www.vagnerrochamartialarts.com/why-our-school")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    '''
    >>> THIS TEST IS NOT VALID BECAUSE THEY ADDED CAPTCHA ON A SIDEBAR CONTACT FORM ON 3/31/2017
        SEE PICTURES IN Sidebar/sidebar_pics<<<<<<<<<
        
    def test_Get_started_valid(self):
        name = self.driver.find_element(By.ID, "input_2_1")
        name.send_keys("Test")
        email = self.driver.find_element(By.ID, "input_2_2")
        email.send_keys("doNotreplytest@gmail.com")
        phone = self.driver.find_element(By.ID, "input_2_3")
        phone.send_keys("1112223333")
        get_started = self.driver.find_element(By.XPATH, ".//*[@id='gform_submit_button_2']")
        get_started.click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("valid_contact.png")
        element = self.driver.find_element(By.XPATH,".//*[@id='post-5544']//h1")
        output = element.text
        print(output)
        if element is not None:
            print("Contact is successful")
        else:
            print("Contact failed")
        self.driver.refresh()
        self.driver.back()
    '''

    def test_WebSpecial_link(self):
        web_special = self.driver.find_element(By.XPATH, ".//*[@id='menu-item-4420']/a")
        web_special.click()
        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)

        if "Web Special" in title:
            print("WEB SPECIAL page is loaded")
        else:
            print("WEB SPECIAL page is NOT loaded")

        '''
        element = self.driver.find_element(By.XPATH, ".//div[@class='entry-content']//h1[text()='WEB SPECIAL']")
        output = element.text
        print("Text is present---> ", output)

        
        '''

if __name__ == '__main__':
    unittest.main(verbosity=2)


