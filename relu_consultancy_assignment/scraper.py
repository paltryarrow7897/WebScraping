from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import pandas as pd
import sys
from tqdm import tqdm

# Start Browser
options = Options()
# options.add_argument("headless")
options.add_argument("log-level=3")
driver = webdriver.Edge(service=Service(
    EdgeChromiumDriverManager().install()), options=options)

# Reading from the CSV, and
# Adding Zeroes before ASIN to make it a string of 10 characters
amazon_df = pd.read_csv("amazon.csv")
amazon_df['Asin'] = amazon_df['Asin'].apply(lambda x: '{0:0>10}'.format(x))

# Setting starting and ending rows from passed arguments
# Allows running multiple scrapers to run simultaneously
start_row = int(sys.argv[1])
end_row = int(sys.argv[2])
df = amazon_df.loc[start_row: end_row]

# Initializing lists and dictionaries to store data
prod_urls = []
prod_categories = []
prod_titles = []
prod_img_urls = []
prod_prices = []
prod_details = []
prod_dict = {"URL": prod_urls,
             "Category": prod_categories,
             "Title": prod_titles,
             "Image URL": prod_img_urls,
             "Price": prod_prices,
             "Details": prod_details
             }

# Main
# tqdm makes a Progress Bar and displays elapsed time, ETA and average time per iteration

# Working
# Loop through each row in the CSV
# Visit each page and try to scrape data
# Put 'N/A' if unable to find something
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Progress"):
    country = row['country']
    asin = row['Asin']

    # Open webpage
    url = f"https://www.amazon.{country}/dp/{asin}"
    driver.get(url)
    driver.implicitly_wait(3)

    try:
        # Check type of product from a div with id 'dp'
        # and get title of the product
        prod_category = driver.find_element(
            By.XPATH, '//*[@id="dp"]').get_attribute("class").split()[0]
        title = driver.find_element(By.CSS_SELECTOR, "#productTitle").text

        # On sample runs, products were found to be of these categories
        # beauty category - 1 product,
        # musical instruments category - 2 products
        # book category - all others

        # Scraping data from product of beauty category
        if prod_category == 'beauty':
            prod_img = driver.find_element(
                By.XPATH, '//*[@id="landingImage"]').get_attribute("src")
            try:
                prod_price = driver.find_element(
                    By.CSS_SELECTOR, '.reinventPricePriceToPayMargin > span:nth-child(2)').text
                prod_detail = driver.find_element(
                    By.ID, 'productDetails_techSpec_section_1').text
            except:
                prod_price = "N/A"
                prod_detail = "N/A"

        # Scraping data from products of musical instruments category
        # Products were out of stock
        elif prod_category == 'musical_instruments':
            prod_img = driver.find_element(
                By.XPATH, '//*[@id="landingImage"]').get_attribute("src")
            try:
                prod_price = driver.find_element(
                    By.CSS_SELECTOR, '#outOfStock > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)').text
                prod_detail = driver.find_element(
                    By.ID, 'productDetails_techSpec_section_1').text
            except:
                prod_price = "N/A"
                prod_detail = "N/A"

        # Scraping data from products of book category
        elif prod_category == 'book':
            prod_img = driver.find_element(
                By.XPATH, '//*[@id="imgBlkFront"]').get_attribute("src")
            try:
                prod_price = driver.find_element(
                    By.CSS_SELECTOR, '#price').text
                prod_detail = driver.find_element(
                    By.ID, "detailBullets_feature_div").text
            except:
                prod_price = "N/A"
                prod_detail = "N/A"

        # If not from above three, put N/A
        else:
            prod_img = "N/A"
            prod_price = "N/A"
            prod_detail = "N/A"

        # Appending scraped data to lists
        prod_urls.append(url)
        prod_categories.append(prod_category)
        prod_titles.append(title)
        prod_img_urls.append(prod_img)
        prod_prices.append(prod_price)
        prod_details.append(prod_detail)

    # If product or URL does not exist
    # put N/A in all columns of that URL
    except:
        prod_urls.append(url)
        prod_categories.append("N/A")
        prod_titles.append("N/A")
        prod_img_urls.append("N/A")
        prod_prices.append("N/A")
        prod_details.append("N/A")

# Saving scraped data in a dataframe
prod_df = pd.DataFrame(prod_dict)
pd.set_option('display.max_rows', None)
prod_df.to_csv(f"scraped_{start_row}_{end_row}.csv")

# Quit Browser
print(prod_df)
driver.quit()
