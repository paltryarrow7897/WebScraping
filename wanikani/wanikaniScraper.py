from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import pandas as pd
import sys

# Open Browser
options = Options()
options.add_argument("headless")
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

arg_1 = sys.argv[1]
arg_2 = sys.argv[2]

start_lvl = 1
end_lvl = 1

if int(arg_1) < int(arg_2) & int(arg_1) > 0:
    start_lvl = int(arg_1)
    end_lvl = int(arg_2)

# Initialize Radical lists and dict
radicals_character = []
radicals_name = []
radicals_mnemonic = []
radicals_level = []
radicals_url = []

radicals_dict = {"Radical":radicals_character, 
                "Name":radicals_name, 
                "Mnemonic":radicals_mnemonic,
                "Level":radicals_level,  
                "URL":radicals_url}

# Initialize Kanji lists and dict
kanjis_character = []
kanjis_meaning = []
kanjis_reading = []
kanjis_mnemonic = []
kanjis_level = []
kanjis_url = []

kanjis_dict = {"Kanji":kanjis_character,
                "Meaning":kanjis_meaning,
                "Reading":kanjis_reading,
                "Mnemonic":kanjis_mnemonic,
                "Level":kanjis_level,
                "URL":kanjis_url}

# Initialize Vocabulary lists and dict
vocabs_character = []
vocabs_meaning = []
vocabs_reading = []
vocabs_mnemonic = []
vocabs_level = []
vocabs_url = []

vocabs_dict = {"Vocabulary":vocabs_character,
                "Meaning":vocabs_meaning,
                "Reading":vocabs_reading,
                "Mnemonic":vocabs_mnemonic,
                "Level":vocabs_level,
                "URL":vocabs_url}

# Functions
def get_radical_url_list():
    RADICAL_LIST_CSS_SELECTOR = f'#level-{i}-radicals > ul > li.character-item'
    RADICAL_XPATH_SELECTOR = f'//*[@id="level-{i}-radicals"]/ul'
    radicals_list_items = driver.find_elements(By.CSS_SELECTOR, RADICAL_LIST_CSS_SELECTOR)        
    for index, radicals_list_item in enumerate(radicals_list_items):
        radical_url = radicals_list_item.find_element(By.XPATH, f'{RADICAL_XPATH_SELECTOR}/li[{index+1}]/a').get_attribute("href")
        RADICAL_URL_LIST.append(radical_url)

def get_kanji_url_list():
    KANJI_LIST_CSS_SELECTOR = f'#level-{i}-kanji > ul > li.character-item'
    KANJI_XPATH_SELECTOR = f'//*[@id="level-{i}-kanji"]/ul'
    kanji_list_items = driver.find_elements(By.CSS_SELECTOR, KANJI_LIST_CSS_SELECTOR)
    for index, kanji_list_item in enumerate(kanji_list_items):
        kanji_url = kanji_list_item.find_element(By.XPATH, f'{KANJI_XPATH_SELECTOR}/li[{index+1}]/a').get_attribute("href")
        KANJI_URL_LIST.append(kanji_url)

def get_vocabulary_url_list():
    VOCABULARY_LIST_CSS_SELECTOR = f'#level-{i}-vocabulary > ul > li.character-item'
    VOCABULARY_XPATH_SELECTOR = f'//*[@id="level-{i}-vocabulary"]/ul'
    vocabulary_list_items = driver.find_elements(By.CSS_SELECTOR, VOCABULARY_LIST_CSS_SELECTOR)
    for index, vocabulary_list_item in enumerate(vocabulary_list_items):
        vocabulary_url = vocabulary_list_item.find_element(By.XPATH, f'{VOCABULARY_XPATH_SELECTOR}/li[{index+1}]/a').get_attribute("href")
        VOCABULARY_URL_LIST.append(vocabulary_url)

def get_radicals():
    RADICAL_CHARACTER_XPATH_SELECTOR = '//*[@id="main"]/body/div[1]/div[3]/div/div/header/h1/span'
    RADICAL_NAME_CSS_SELECTOR = '#information > div > p'
    RADICAL_MNEMONIC_CSS_SELECTOR = '#information > section'

    for index, page in enumerate(RADICAL_URL_LIST):
        driver.get(page)
        driver.implicitly_wait(5)
        
        radical_character = driver.find_element(By.XPATH, RADICAL_CHARACTER_XPATH_SELECTOR).text
        radical_name = driver.find_element(By.CSS_SELECTOR, RADICAL_NAME_CSS_SELECTOR).text
        radical_mnemonic = driver.find_element(By.CSS_SELECTOR, RADICAL_MNEMONIC_CSS_SELECTOR).text

        radicals_character.append(radical_character)
        radicals_name.append(radical_name)
        radicals_mnemonic.append(radical_mnemonic)
        radicals_level.append(i)
        radicals_url.append(page)

def get_kanji():
    KANJI_CHARACTER_XPATH_SELECTOR = '//*[@id="main"]/body/div[1]/div[3]/div/div/header/h1/span'
    KANJI_MEANING_CSS_SELECTOR = '#meaning > div > p'
    KANJI_MNEMONIC_CSS_SELECTOR = '#meaning > section'
    KANJI_READING_CSS_SELECTOR = '#reading > section'

    for index, page in enumerate(KANJI_URL_LIST):
        driver.get(page)
        driver.implicitly_wait(5)

        kanji_character = driver.find_element(By.XPATH, KANJI_CHARACTER_XPATH_SELECTOR).text
        kanji_meaning = driver.find_element(By.CSS_SELECTOR, KANJI_MEANING_CSS_SELECTOR).text
        kanji_reading = driver.find_element(By.CSS_SELECTOR, KANJI_READING_CSS_SELECTOR).text
        kanji_mnemonic = driver.find_element(By.CSS_SELECTOR, KANJI_MNEMONIC_CSS_SELECTOR).text

        kanjis_character.append(kanji_character)
        kanjis_meaning.append(kanji_meaning)
        kanjis_reading.append(kanji_reading)
        kanjis_mnemonic.append(kanji_mnemonic)
        kanjis_level.append(i)
        kanjis_url.append(page)

def get_vocabulary():
    VOCAB_CHARACTER_XPATH_SELECTOR = '//*[@id="main"]/body/div[1]/div[3]/div/div/header/h1/span'
    VOCAB_MEANING_CSS_SELECTOR = '#meaning > div:nth-child(2) > p'
    VOCAB_READING_CSS_SELECTOR = '#reading > section'
    VOCAB_MNEMONIC_CSS_SELECTOR = '#meaning > section'

    for index, page in enumerate(VOCABULARY_URL_LIST):
        driver.get(page)
        driver.implicitly_wait(5)

        vocab_character = driver.find_element(By.XPATH, VOCAB_CHARACTER_XPATH_SELECTOR).text
        vocab_meaning = driver.find_element(By.CSS_SELECTOR, VOCAB_MEANING_CSS_SELECTOR).text
        vocab_reading = driver.find_element(By.CSS_SELECTOR, VOCAB_READING_CSS_SELECTOR).text
        vocab_mnemonic = driver.find_element(By.CSS_SELECTOR, VOCAB_MNEMONIC_CSS_SELECTOR).text

        vocabs_character.append(vocab_character)
        vocabs_meaning.append(vocab_meaning)
        vocabs_reading.append(vocab_reading)
        vocabs_mnemonic.append(vocab_mnemonic)
        vocabs_level.append(i)
        vocabs_url.append(page)

# Main
for i in range(start_lvl, end_lvl+1):
    url = f'https://www.wanikani.com/level/{i}'

    driver.get(url)
    driver.implicitly_wait(5)

    RADICAL_URL_LIST = []
    KANJI_URL_LIST = []
    VOCABULARY_URL_LIST = []

    # Get lists of Radical, Kanji and Vocabulary URLs
    get_radical_url_list()
    get_kanji_url_list()
    get_vocabulary_url_list()

    # Get information of Radical, Kanji and Vocabulary
    get_radicals()
    get_kanji()
    get_vocabulary()

# Write to DataFrame and then CSV
radicals_df = pd.DataFrame(radicals_dict)
kanjis_df = pd.DataFrame(kanjis_dict)
vocabs_df = pd.DataFrame(vocabs_dict)

radicals_df.to_csv(f"radical_{start_lvl}_{end_lvl}.csv")
kanjis_df.to_csv(f"kanji_{start_lvl}_{end_lvl}.csv")
vocabs_df.to_csv(f"vocabulary_{start_lvl}_{end_lvl}.csv")

driver.quit()