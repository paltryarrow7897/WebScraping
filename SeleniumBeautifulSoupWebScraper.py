from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

import pandas as pd
import time

# Open Browser
options = Options()
options.add_argument("headless")
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

for i in range(1,6):
    url = f'https://www.wanikani.com/level/{i}'

    driver.get(url)
    driver.implicitly_wait(5)

    RADICAL_CSS_SELECTOR = f'#level-{i}-radicals > ul > li.character-item'
    KANJI_CSS_SELECTOR = f'#level-{i}-kanji > ul > li.character-item'
    VOCABLUARY_CSS_SELECTOR = f'#level-{i}-vocabulary > ul > li.character-item'
    
    RADICAL_XPATH_SELECTOR = f'//*[@id="level-{i}-radicals"]/ul'
    KANJI_XPATH_SELECTOR = f'//*[@id="level-{i}-kanji"]/ul'
    VOCABULARY_XPATH_SELECTOR = f'//*[@id="level-{i}-vocabulary"]/ul'

    title = driver.title
    radicals_list_items = driver.find_elements(By.CSS_SELECTOR, RADICAL_CSS_SELECTOR)
    kanji_list_items = driver.find_elements(By.CSS_SELECTOR, KANJI_CSS_SELECTOR)
    vocabulary_list_items = driver.find_elements(By.CSS_SELECTOR, VOCABLUARY_CSS_SELECTOR)

    print()
    print(title)
    print(f"Radicals: {len(radicals_list_items)}")
    print(f"Kanji: {len(kanji_list_items)}")
    print(f"Vocabulary: {len(vocabulary_list_items)}")

    # Radicals
    print()
    print("Radicals:")
    for index, radicals_list_item in enumerate(radicals_list_items):
        radical_character = radicals_list_item.find_element(By.XPATH, f'{RADICAL_XPATH_SELECTOR}/li[{index+1}]/a/span').text
        radical_name = radicals_list_item.find_element(By.XPATH, f'{RADICAL_XPATH_SELECTOR}/li[{index+1}]/a/ul/li[2]').text
        radical_url = radicals_list_item.find_element(By.XPATH, f'{RADICAL_XPATH_SELECTOR}/li[{index+1}]/a').get_attribute("href")
        print(f"({index+1}) Radical = {radical_character}, Name = {radical_name}, URL = {radical_url}")

    # Kanji
    print()
    print("Kanji:")
    for index, kanji_list_item in enumerate(kanji_list_items):
        kanji_character = kanji_list_item.find_element(By.XPATH, f'{KANJI_XPATH_SELECTOR}/li[{index+1}]/a/span').text
        kanji_reading = kanji_list_item.find_element(By.XPATH, f'{KANJI_XPATH_SELECTOR}/li[{index+1}]/a/ul/li[1]').text
        kanji_meaning = kanji_list_item.find_element(By.XPATH, f'{KANJI_XPATH_SELECTOR}/li[{index+1}]/a/ul/li[2]').text
        kanji_url = kanji_list_item.find_element(By.XPATH, f'{KANJI_XPATH_SELECTOR}/li[{index+1}]/a').get_attribute("href")
        print(f"({index+1}) Kanji = {kanji_character}, Reading = {kanji_reading}, Name = {kanji_meaning}, URL = {kanji_url}")

    # Vocabulary
    print()
    print("Vocabulary:")
    for index, vocabulary_list_item in enumerate(vocabulary_list_items):
        vocabulary_character = vocabulary_list_item.find_element(By.XPATH, f'{VOCABULARY_XPATH_SELECTOR}/li[{index+1}]/a/span').text
        vocabulary_reading = vocabulary_list_item.find_element(By.XPATH, f'{VOCABULARY_XPATH_SELECTOR}/li[{index+1}]/a/ul/li[1]').text
        vocabulary_meaning = vocabulary_list_item.find_element(By.XPATH, f'{VOCABULARY_XPATH_SELECTOR}/li[{index+1}]/a/ul/li[2]').text
        vocabulary_url = vocabulary_list_item.find_element(By.XPATH, f'{VOCABULARY_XPATH_SELECTOR}/li[{index+1}]/a').get_attribute("href")
        print(f"({index+1}) Vocabulary = {vocabulary_character}, Reading = {vocabulary_reading}, Name = {vocabulary_meaning}, URL = {vocabulary_url}")

driver.quit()