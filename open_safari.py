from selenium import webdriver
"""
Web automation with Selenium and Python
Safari: Don't forget to enable the automation of the browser into the developer options
"""

driver = webdriver.Safari()
driver.get('https://www.wishtrip.com/home')
print(driver.title)
driver.close()

