from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest


class CraigsSporting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        url = ("https://miami.craigslist.org/search/brw/sss")
        cls.driver.get(url)
        

    def test_1_ping_pong(self):
        element = self.driver.find_element(By.ID, "query")
        element.send_keys("table tennis")
        btn = element = self.driver.find_element(By.CSS_SELECTOR, ".searchbtn.changed_input.clickme")
        btn.click()
        time.sleep(5)
        #self.driver.get_screenshot_as_file("pong.jpg")
        destinationFileName = 'C:\\Users\\CSR\\Desktop\\table.png'
        self.driver.save_screenshot(destinationFileName)

    def test_2_outdoor_table_tennis(self):

        month_drop = self.driver.find_element(By.ID, "subcatAbb")
        Select(month_drop).select_by_value("sga")
        element = self.driver.find_element(By.ID, "query")
        element.clear()
        element.send_keys("outdoor ping pong table")
        btn = element = self.driver.find_element(By.CSS_SELECTOR, ".searchbtn.changed_input.clickme")
        btn.click()
        time.sleep(2)
        destinationFileName = 'C:\\Users\\CSR\\Desktop\\outdoor.png'
        self.driver.save_screenshot(destinationFileName)

        #self.driver.get_screenshot_as_file("outdoor.jpg")

    def test_3_ping_pong_table(self):
        element = self.driver.find_element(By.ID, "query")
        element.clear()
        element.send_keys("ping pong table")
        btn = element = self.driver.find_element(By.CSS_SELECTOR, ".searchbtn.changed_input.clickme")
        btn.click()
        time.sleep(5)
        #self.driver.get_screenshot_as_file("pong.jpg")
        destinationFileName = 'C:\\Users\\CSR\\Desktop\\pong.png'
        self.driver.save_screenshot(destinationFileName)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(verbosity=2)
