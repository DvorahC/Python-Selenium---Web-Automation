import unittest
from selenium import webdriver

'''''
Automatic test to check some buttons and functions of the homepage
'''''


class HomePage(unittest.TestCase):

    def test_title(self):
        home_page = webdriver.Chrome('/Applications/chromedriver')
        home_page.get('https://www.wishtrip.com/home')
        self.assertTrue('WishTrip - Travel Experience Network', home_page.title)
        print('test1 pass')
        home_page.close()

    def test_get_all_languages_list(self):
        home_page = webdriver.Chrome('/Applications/chromedriver')
        home_page.get('https://www.wishtrip.com/home')
        language_button = home_page.find_element_by_class_name('page-footer__website-locale__selected__lang')
        language_button.click()
        language_menu = home_page.find_element_by_class_name('page-footer__website-locale__menu')
        self.assertIn('Spanish', language_menu.text)
        print('test 2 pass')
        home_page.close()


if __name__ == '__main__':
    unittest.main()
