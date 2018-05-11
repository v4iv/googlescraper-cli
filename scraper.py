import csv

from selenium import webdriver
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Firefox()
    return driver


def scrape_google(driver, query, limit=10):
    driver.get(
        'https://www.google.com/search?gl=us&hl=en&pws=0&gws_rd=cr&q=' + query + '&num=' + str(limit) + '&ie=utf-8&oe=utf-8')
    try:
        filename = 'google_scrape_results-%s.csv' % query
        with open(filename, 'w+') as f:
            writer = csv.writer(f)
            results = driver.find_elements_by_css_selector("h3.r a")
            for result in results:
                title = result.text
                link = result.get_property("href")
                writer.writerow((title, link))
    except TimeoutException:
        print("Google Scraping Failed")
