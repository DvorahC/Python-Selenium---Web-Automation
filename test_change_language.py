import unittest
from selenium import webdriver

'''''
Automatic test to confirm language is changed in website
'''''


class MyTestCase(unittest.TestCase):
    def test_change_language(self):
        home_page = webdriver.Chrome('/Applications/chromedriver')
        home_page.get('https://www.wishtrip.com/home')
        language_button = home_page.find_element_by_class_name('page-footer__website-locale__selected__lang')
        language_button.click()
        language_menu = home_page.find_element_by_class_name('page-footer__website-locale__menu')
        language_french = language_menu.find_element_by_id('lang-fr')
        language_french.click()
        home_page.implicitly_wait(30)
        page_footer = home_page.find_element_by_class_name("page-footer__content")
        self.assertIn('Contactez-nous', page_footer.text)
        print('language changed - test pass')
        home_page.close()


if __name__ == '__main__':
    unittest.main()
