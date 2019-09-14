import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''''
Automatic test to run 2 test in the search bar 
use of setUpClass and tearDownClass in order to avoid relaunching the browser at each test
'''''


class Search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/Applications/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.wishtrip.com/home")

    def test_title(self):
        self.assertTrue('WishTrip - Travel Experience Network', self.driver.title)

    def test_search_bar(self):
        self.search_button = self.driver.find_element_by_id('search-input')
        self.search_button.send_keys('Jerusalem')
        self.driver.implicitly_wait(20)
        self.search_button.send_keys(Keys.ENTER)
        search_page = self.driver.find_element_by_class_name("search-tabs__tabs-container__tab")
        self.assertTrue('TREK', search_page.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
