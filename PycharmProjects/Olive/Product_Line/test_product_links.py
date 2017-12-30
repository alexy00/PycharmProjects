from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class Product(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = ("http://lolivebleue.com")
        cls.driver.get(page_url)




    def test_olive1(self):

        prod = self.driver.find_element(By.XPATH, ".//ul[@id='primary-parallax-menu']//a[text()='Product']")
        prod.click()
        time.sleep(2)

        olive1 = self.driver.find_element(By.XPATH, ".//ul[@id='psProjects']//a[@href='http://lolivebleue.com/olive1/']")
        olive1.click()
        time.sleep(2)

        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)

        if "Olive1" in title:
            print("OLIVE1 page is loaded")
        else:
            print("OLIVE1 page is NOT loaded")


    def test_olive2(self):

        prod = self.driver.find_element(By.XPATH, ".//ul[@id='primary-parallax-menu']//a[text()='Product']")
        prod.click()
        time.sleep(2)

        olive2 = self.driver.find_element(By.XPATH, ".//ul[@id='psProjects']//a[@href='http://lolivebleue.com/olive2/']")
        olive2.click()
        time.sleep(2)

        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)

        if "Olive2" in title:
            print("OLIVE2 page is loaded")
        else:
            print("OLIVE2 page is NOT loaded")


    def test_olive3(self):

        prod = self.driver.find_element(By.XPATH, ".//ul[@id='primary-parallax-menu']//a[text()='Product']")
        prod.click()
        time.sleep(2)

        olive3 = self.driver.find_element(By.XPATH, ".//ul[@id='psProjects']//a[@href='http://lolivebleue.com/olive3/']")
        olive3.click()
        time.sleep(2)

        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)

        if "Olive3" in title:
            print("OLIVE3 page is loaded")
        else:
            print("OLIVE3 page is NOT loaded")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
