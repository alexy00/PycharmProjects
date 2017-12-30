from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


import unittest

class Header(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.driver.get("https://www.vagnerrochamartialarts.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_Programs_tab(self):

        Programs_link = self.driver.find_element(By.XPATH,".//ul[@id='top-menu']//a[text()='Programs']")
        action = ActionChains(self.driver)
        action.move_to_element(Programs_link).perform()
        dropDown = self.driver.find_element(By.XPATH,".//*[@id='menu-item-29']/ul")
        if dropDown is not None:
            print("Mouse Hovered on PROGRAMS link")
        else:
            print("Mouse Hover failed")

        dropDownOption = self.driver.find_element(By.XPATH,"//ul[@id='top-menu']//a[text()='Seminars']")
        action.move_to_element(dropDownOption).click().perform()
        element = self.driver.find_element(By.XPATH,".//*[@id='post-97']//h1[text()='MARTIAL ARTS & SELF DEFENSE SEMINARS']")

        if element is not None:
            print("Mouse clicked on SEMINARS link")
        else:
            print("Mouse failed to click on SEMINARS link")


    def test_Home_tab(self):

        Home_link = self.driver.find_element(By.XPATH,".//*[@id='menu-item-30']/a")
        Home_link.click()
        print("URL-> ", self.driver.current_url)
        print("Title of this page-> ", self.driver.title)

        Logo = self.driver.find_element(By.ID, "logo")
        if Logo is not None:
            print("Vagner Rocha Martial Arts logo is visible on a header")
        else:
            print("Vagner Rocha Martial Arts logo should be visible on a header. Please check specification")

    
    def test_Why_Our_School_tab(self):
        Why_Our_School_link = self.driver.find_element(By.XPATH,".//*[@id='menu-item-27']/a")
        Why_Our_School_link.click()
        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)
        element = self.driver.find_element(By.XPATH, ".//article[@id='post-16']//h1[text()='WHY CHOOSE OUR MARTIAL ARTS SCHOOL']")
        result = element.is_displayed()
        assert result == True




if __name__ == '__main__':
    unittest.main(verbosity=2)
