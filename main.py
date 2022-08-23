from selenium import webdriver
from dotenv import load_dotenv
import os
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


#Take environment variables from .env
load_dotenv()

path = os.getenv("DRIVER_PATH")

options = Options()
options.headless = True

service = Service(executable_path=str(path))
driver = webdriver.Chrome(service=service, options=options)
nameList = []
hashList = []
pages = range(100)

for page in reversed(pages):

    website = f'https://nyaa.si/user/puyero?p={page + 1}'
    driver.get(website)

    trList = driver.find_elements(by = "xpath", value='//tbody/tr')

    for line in trList:

        title = line.find_element(by="xpath", value='./td[@colspan="2"]/a[not(@class="comments")]')
        link = line.find_elements(by="xpath", value='./td[@class="text-center"]/a')

        nameList.append(title.text)
        hashList.append(link[1].get_attribute("href")[20:60])

animeData = { "tittle" : nameList, "hash" : hashList}

csv_test = pd.DataFrame(animeData)
csv_test.to_csv("puyasubs-hash.csv")

driver.quit()
