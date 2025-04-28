from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def init_driver():
    options = Options()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

def collect_page_data(driver, url):
    driver.get(url)
    time.sleep(2)
    data = {
        "pages": [{
            "url": url,
            "page_title": driver.title,
            "load_time": 2000,
            "console_errors": [],
            "elements": {
                "buttons": driver.find_elements(By.TAG_NAME, 'button'),
                "links": driver.find_elements(By.TAG_NAME, 'a')
            }
        }]
    }
    return data