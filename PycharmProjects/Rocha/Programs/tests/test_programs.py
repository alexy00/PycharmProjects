from selenium import webdriver
from selenium.webdriver.common.by import By


import unittest

class ProgramsPage(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = ("https://www.vagnerrochamartialarts.com/martial-arts-programs")
        cls.driver.get(page_url)



    def test_Adults_Teens_BJJ_ReadMore_link(self):
        Read_More_link = self.driver.find_element(By.XPATH,".//a[@title='Brazilian Jiu-Jistu' and contains(text(),'Read More')]")
        Read_More_link.click()
        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)

        self.driver.back()



    def test_MMA_Program_ReadMore_link(self):
        Read_More_link = self.driver.find_element(By.XPATH,".//a[@title='Mixed Martial Arts' and contains (text(), 'Read More')]")
        Read_More_link.click()
        print("New page opened. URL-> ", self.driver.current_url)
        title = self.driver.title
        print("Title of page is: ", title)

        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
