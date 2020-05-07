# Web scraping with Selenium and Python
# Source: https://app.pluralsight.com/guides/implementing-web-scraping-with-selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

# Configure Chrome Webdriver
def configure_chrome_driver():
    # Additional Options to webdriver
    chrome_options = ChromeOptions()
    # make browser headless
    chrome_options.add_argument("--headless")
    # Instantiate Webdriver
    # chromedriver.exe is already in PATH
    driver = webdriver.Chrome("chromedriver.exe", options = chrome_options)
    return driver

def loadAllContent(driver):
    WebDriverWait(driver, 5).until(
        lambda s: s.find_element_by_class_name("cookie_notification").is_displayed()
    )
    driver.find_element_by_class_name("cookie_notification--opt_in").click()
    while True:
        try:
            WebDriverWait(driver, 3).until(
                lambda s: s.find_element_by_id('search-result-section-load-more').is_displayed()
            )
        except TimeoutException:
            break
        driver.find_element_by_id('search-result-section-load-more').click()

def getCourses(driver, search_keyword):
    # Step 1: Go to website
    driver.get(f"https://www.pluralsight.com/search?q={search_keyword}&categories=course")
    WebDriverWait(driver, 5).until(
        lambda s: s.find_element_by_id("search_results-category-target").is_displayed()
    )

    # Load all page data by clicking Load More button...
    loadAllContent(driver)

    # Step 2: Create a parse tree of page sourrces
    soup = BeautifulSoup(driver.page_source, "lxml")

    # Step 3: Iterate over the search result and fetch course
    for course_page in soup.select("div.search-results-page"):
        for course in course_page.select("div.search-result"):
            # selectors for required info
            title_selector = "div.search-result__info div.search-result__title a"
            author_selector = "div.search-result__details div.search-result__author"
            level_selector = "div.search-result__details div.search-result__level"
            length_selector = "div.search-result__details div.search-result__length"
            print({
                "title": course.select_one(title_selector).text,
                "author": course.select_one(author_selector).text,
                "level": course.select_one(level_selector).text,
                "length": course.select_one(length_selector)
            })

# def getAuthors(driver, search_keyword):

def login(driver, credentials):
    driver.get("https://app.pluralsight.com/")
    uname_element = driver.find_element_by_name("Username")
    uname_element.send_keys(credentials["username"])

    pwd_element = driver.find_element_by_name("Password")
    pwd_element.send_keys(credentials["password"])

    login_btn = driver.find_element_by_id("login")
    login_btn.click()

# Driver code
# create driver object
driver = configure_chrome_driver()
search_keyword = "Selenium"
getCourses(driver, search_keyword)
# close driver
driver.close()