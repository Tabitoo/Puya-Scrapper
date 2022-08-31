from selenium import webdriver
from dotenv import load_dotenv
import time
import os
import pandas as pd
from utils.utils import get_chapter
from kitsu.getAnime import getByName
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


#Take environment variables from .env
load_dotenv()

path = os.getenv("DRIVER_PATH")

options = Options()
options.headless = True

service = Service(executable_path=str(path))
driver = webdriver.Chrome(service=service, options=options)
count = 0
nameList = []
hashList = []
chapterList = []
kitsu_id_list = []
pages = range(100)

for page in reversed(pages):

    website = f'https://nyaa.si/user/puyero?p={page + 1}'
    driver.get(website)

    trList = driver.find_elements(by = "xpath", value='//tbody/tr')

    count = count + 1

    if count == 10:
        count = 0
        print('Se paro el codigo por 5 minutos')
        time.sleep(300)
        print('Sigue la ejecucion del codigo...')

    for line in trList:

        title = line.find_element(by="xpath", value='./td[@colspan="2"]/a[not(@class="comments")]')
        link = line.find_elements(by="xpath", value='./td[@class="text-center"]/a')

        nameList.append(title.text)
        hashList.append(link[1].get_attribute("href")[20:60])
        chapterList.append(get_chapter(title.text))
        kitsu_id_list.append(getByName(title.text))

animeData = { "tittle" : nameList, "hash" : hashList, "chapter" : chapterList, "kitsu_id" : kitsu_id_list}

csv_test = pd.DataFrame(animeData)
csv_test.to_csv("puyasubs-hash.csv")

driver.quit()
