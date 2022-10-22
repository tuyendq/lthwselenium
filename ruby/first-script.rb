require 'webdrivers'
# require 'spec_helper'

RSpec.describe 'First script' do
    it 'uses eight components' do
        # 1. Start the session
        driver = Selenium::WebDriver.for :firefox

        # 2. Take action on browser
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')

        # 3. Request browser information
        title = driver.title

        # 4. Establish waiting strategy
        driver.manage.timeouts.implicit_wait = 500

        # 5. Find an element
        text_box = driver.find_element(name: 'my-text')
        submit_button = driver.find_element(tag_name: 'button')

        # 6. Take action on element
        text_box.send_keys('Selenium')
        submit_button.click

        # 7. Request element information
        message = driver.find_element(id: 'message')
        value = message.text
        expect(value).to eq('Received!')

        # 8. End the session
        driver.quit
    end
end
