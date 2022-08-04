## About
Python Task of scraping data from 1000 Amazon links using Selenium.

## Files
_`amazon.csv`_ - Table of links to scrape.
_`scraper.py`_ - Python script to scrape data from web pages.
_`scraped_full.csv`_ - Table of all scraped data from rows 0 to 999. This file shows the Python script is unable to work for 1000 rows as a lot of data is lost.
_`scraped_merged.csv`_ - Merged table of scraped data of 100 rows, i.e, 0-99, 100-199, 200-299, etc. All these files can be seen in _`CSV files/`_.
_`scraped_merged.json`_ - _`scraped_merged.csv`_ converted to JSON.

## Usage
Install requirements from `requirements.txt`.
I use Microsoft Edge so Selenium uses Edge Web Driver.
You'll need to have Edge installed or change Web Driver inside `scraper.py`.

Usage - `python3 scraper.py <start_row_in_amazon.csv> <end_row_in_amazon.csv>`
Output is a CSV file with name of the format - `scraper_<start_row>_<end_row>.csv`

For example, to scrape the first 100 rows, use `python3 scraper.py 0 99`
And output is saved to `scraper_0_99.csv`

## Steps taken
* Observed `amazon.csv` to see how data is stored. 
* ASIN field looked wrong as on manually visiting many links, no products were found. 
* Converted ASIN to a 10 character string with starting zeros.
* Visited webpages to see the page sources. Found page source was different for a product category.
* Found out there are 3 categories - beauty, book and muscial instruments inside the provided data. 
* Most data belongs to `book`. Visited links to see page source and find elements to scrape from.
* Most webpages had identical structure, Scraped title, category, image URL, price, and details.
* First, Tried scraping all links in 1 go. It took over 1 hour and also resulted in lost data.
* Then Tried scraping only 100 rows at a time.
* To do this I ran `python3 scraper.py 0 99` ... `python3 scraper.py 900 999` to create 10 CSV files.
* Some pages were not scraped. Data which couldn't be scraped was marked as 'N/A'.
* These 10 CSV files were then merged using `pd.concat()` to create `scraped_merged.csv`.
* Only 1 URL (row 4) was found to have no product represented by all 'N/A's in `scraped_merged.csv`.
* The CSV was converted to JSON on https://csvjson.com/csv2json. Result as `scraped_merged.json`.
* Time taken by script for every 100 rows:
    + 000 - 099 06:31
    + 100 - 199 05:46
    + 200 - 299 05:13
    + 300 - 399 06:04
    + 400 - 499 06:03
    + 500 - 599 05:21
    + 600 - 699 06:53
    + 700 - 799 06:43
    + 800 - 899 07:26
    + 900 - 999 07:02
* Average: 06 mins 18 secs.
