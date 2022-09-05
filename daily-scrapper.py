from selenium import webdriver
from dotenv import load_dotenv
import os
from deta import Deta
from kitsu.getAnime import getByName
from utils.utils import  get_chapter
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#Take environment variables from .env
load_dotenv()

deta_key = os.getenv("DETA_BASE_KEY")

deta = Deta(str(deta_key))

db = deta.Base("puyasubs-hash")


path = os.getenv("DRIVER_PATH")

options = Options()
options.headless = True

service = Service(executable_path=str(path))
driver = webdriver.Chrome(service=service, options=options)
animeData = []

website = 'https://nyaa.si/user/puyero?p=1'
driver.get(website)

trList = driver.find_elements(by = "xpath", value='//tbody/tr')

for line in trList:

    title = line.find_element(by="xpath", value='./td[@colspan="2"]/a[not(@class="comments")]')
    link = line.find_elements(by="xpath", value='./td[@class="text-center"]/a')

    request_data = db.fetch({"title" : title.text})

    if not request_data.count >= 1:

        db.put({"title" : title.text, "hash": link[1].get_attribute("href")[20:60], "chapter" : get_chapter(title.text), "kitsu_id" : getByName(title.text)})

driver.quit()

