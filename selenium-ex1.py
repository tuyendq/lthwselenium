from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://google.com')

el = driver.find_element_by_name('q')

el.send_keys('anh em cay khe')

from selenium.webdriver.common.keys import Keys

el.send_keys(Keys.RETURN)