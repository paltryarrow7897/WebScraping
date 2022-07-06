mdcomputers is a PC components website.

Idea behind doing this was to see which parts are available at what price.

Fortunately the website only lists in-stock items and therefore I only needed to scrape the name of the product with its current price.

Usage: 

python3 mdcomputersScraper.py < category >

For example, for GPU:
python3 mdcomputersScraper.py graphics-card

The script creates a CSV file of the < category > after running.