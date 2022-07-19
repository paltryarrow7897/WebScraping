# About WaniKani

WaniKani is a web application that helps people learn Japanese kanji and associated vocabulary. 
It uses radicals, mnemonics, and a spaced repetition learning system in order to help its users memorize the characters and vocabulary more effectively.

WaniKani divides radicals, kanji and vocabulary into levels from 1 to 60.
The first 3 levels are free so go try them out. Rest are available by subscriptions.

# About this script

This script finds all radicals, kanji and vocabulary in a given level.
Result is saved in 3 CSV files, one each for radicals, kanji and vocabulary.

# Usage

I primarily use Microsoft Edge so my script uses Edge Web Driver for Selenium. 
You'll need to have Edge, Selenium and Webdriver Manager installed to run this script.
Other requisites are pandas and tqdm.

Run the script with 2 arguments, first is the start level, second is the end level.
For example, to get all radicals, kanji and vocabulary from level 1 to 60, run

python3 wanikaniScraper.py 1 60

Or to get everything from the free first 3 levels, run

python3 wanikaniScraper.py 1 3

Output files are named as [radical/kanji/vocabulary]_{start_level}_{end_level}.csv

Warning: Getting all items from level 1 to 60 from a single script will take forever to run.
Run multiple scripts instead.

Multiple scripts can be started independently. 
Just change passing arguments. For example, running 

    python3 wanikaniScraper.py 1 1
    python3 wanikaniScraper.py 2 2

in different consoles will start scraping level 1 and level 2 items simultaneosly.

Errors are not handled yet, so anything unexpected results with an open Selenium web driver.
