from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains




class Plan_Your_Vacation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        page_url = ("https://www.ncl.com/")
        cls.driver.get(page_url)
        try:
            pop_up = cls.driver.find_element(By.XPATH, "//map[@name='IPEMap']/area[@alt='close']")
            pop_up.click()
        except:
            pass



    def test_1_4Guests(self):
        driver = self.driver
        plan_vacation_menu = driver.find_element(By.CSS_SELECTOR, ".menu-42726.menu_clearfix>a")
        cruise_search_dropdown = driver.find_element(By.CSS_SELECTOR, ".menu-42742>a")
        action = ActionChains(driver)
        action.move_to_element(plan_vacation_menu).perform()
        action.move_to_element(cruise_search_dropdown).click().perform()
        time.sleep(2)

        try:
            pop_up = driver.find_element(By.ID, "simplemodal-close-img")
            pop_up.click()
        except:
            pass
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".search-select.ng-binding").click()
        driver.find_element(By.XPATH, "//li[text()='4 Guests']").click()
        self.assertIn("4-guests", driver.current_url)
        print("\nNews page is loaded when 4 Guessts is selected")
        print(driver.current_url)


    def test_2_Sort_By_Price(self):
        driver = self.driver
        time.sleep(2)
        wait = WebDriverWait(driver, 20, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' Featured ']")))

        element.click()
        driver.find_element(By.XPATH, "//li[text()=' Price ']").click()

        self.assertIn("sortBy=Price", driver.current_url)
        print("\nNews page is loaded when Sort by: Price is selected")
        print(driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
