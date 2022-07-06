from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import re
import pandas as pd
import sys

item_names = []
item_prices = []
items = {"Name":item_names, "Price":item_prices}

# Set headless option
options = Options()
options.add_argument("headless")
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

# Set which item category to scrape
def set_url(section):
    return f"https://mdcomputers.in/{section}"

# Open Browser
url = set_url(str(sys.argv[1]))
driver.get(url)
driver.implicitly_wait(5)

# XPATH Selectors
ITEM_NAME_XPATH_SELECTOR = '//*[@id="content"]/div[2]/div[2]'
ITEM_PRICE_XPATH_SELECTOR = '//*[@id="content"]/div[2]/div[2]'
ITEM_COUNT_XPATH_SELECTOR = '//*[@id="content"]/div[2]/div[3]/div/div[2]'

# Regex for finding number of items and pages
exp = r"\w+ (\d+) \w+ (\d+) \w+ \d+ \((\d+)"

# Return number of pages of the category
def find_item_pages():
    item_search = re.search(exp, driver.find_element(By.XPATH, ITEM_COUNT_XPATH_SELECTOR).text)
    return int(item_search.group(3))

# Return number of items of the category on the current page
def find_items_on_this_page():
    item_search = re.search(exp, driver.find_element(By.XPATH, ITEM_COUNT_XPATH_SELECTOR).text)
    page_start = int(item_search.group(1))
    page_end = int(item_search.group(2))
    return page_end - page_start + 1

# Loop over each page of the category
item_pages = find_item_pages()
for i in range(item_pages):
    page_url = f'{url}?page={i+1}'
    driver.get(page_url)
    driver.implicitly_wait(5)

    # Loop over each item of the category on the current page
    items_on_this_page = find_items_on_this_page()
    for index in range(items_on_this_page):
        item_name = driver.find_element(By.XPATH, f'{ITEM_NAME_XPATH_SELECTOR}/div[{index+1}]/div/div[2]/h4/a').text
        item_price = int(driver.find_element(By.XPATH, f'{ITEM_PRICE_XPATH_SELECTOR}/div[{index+1}]/div/div[2]/div[2]/span[1]').text[1:].replace(",",""))
        
        item_names.append(item_name)
        item_prices.append(item_price)

# Save to CSV
df = pd.DataFrame(data=items)
df.to_csv(f"{url[23:]}.csv")

# Close Browser
driver.quit