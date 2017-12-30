from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class Links(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = ("http://www.lifecellskin.com/")
        cls.driver.get(page_url)
        try:     #  <------TO CLICK THE POP UP
            cls.driver.find_element_by_css_selector(".//div[@id='SnapABug_P']//img[@alt='Close']").click()
        except:
            pass
    def test_All_in_one(self):

        Shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-290>a")
        Shop.click()
        time.sleep(2)
        allInOne = self.driver.find_element(By.XPATH, ".//section[@id='all-products-panel']//h2[text()='South Beach Skincare: All In One Anti-Aging Treatment 2.54 oz']")
        allInOne.click()
        time.sleep(2)

        print("\n")
        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)

        if "Anti-Aging Cream an All-in-One" in title:
            print("Anti-Aging Cream an All-in-One Wrinkle Treatment page is loaded")
        else:
            print("Anti-Aging Cream an All-in-One Wrinkle Treatment page is NOT loaded")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(verbosity=2)
