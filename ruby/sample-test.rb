require "webdrivers"

driver = Selenium::WebDriver.for :firefox
driver.navigate.to "https://google.com"

element = driver.find_element(name: 'q')
element.click
element.send_keys "Hello WebDriver!"
element.submit

driver.quit