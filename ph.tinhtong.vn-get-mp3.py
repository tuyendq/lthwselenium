from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up Chrome options to run headless (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set up the WebDriver (make sure you have the correct driver installed)
driver = webdriver.Chrome(options=chrome_options)  # You can use Firefox, Edge, etc.


# Open the website
url = "https://ph.tinhtong.vn/Home/MP3?p=MP3*-+Duc+Dat+Lai+Lat+Ma*Cam+Nang+Cho+Cuoc+Song"  # Replace with the desired URL
driver.get(url)

# Wait until an element is visible
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.mdtc-clnplra-playlist")))


# Find an element (modify the selector based on the website structure)
# element = driver.find_element(By.TAG_NAME, "h1")
element = driver.find_element(By.CSS_SELECTOR, "div.mdtc-clnplra-playlist")
list_items = element.find_elements(By.TAG_NAME, "li")
for item in list_items:
    item_text = item.find_element(By.CSS_SELECTOR, "span:nth-child(3)").text
    item_link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
    print(f"Title: {item_text}, Link: {item_link}")


# Close the browser
driver.quit()