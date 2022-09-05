from selenium import webdriver
from dotenv import load_dotenv
import time
import os
import pandas as pd
from utils.utils import get_chapter
from kitsu.getAnime import getByName
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from deta import Deta

load_dotenv()

deta_key = os.getenv("DETA_BASE_KEY")

deta = Deta(str(deta_key))

db = deta.Base("puyasubs-hash")

path = os.getenv("DRIVER_PATH")

options = Options()
options.headless = True

service = Service(executable_path=str(path))
driver = webdriver.Chrome(service=service, options=options)
count = 0
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

        db.put({"title" : title.text, "hash": link[1].get_attribute("href")[20:60], "chapter" : get_chapter(title.text), "kitsu_id" : getByName(title.text)})


driver.quit()
