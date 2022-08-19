from selenium import webdriver
from dotenv import load_dotenv
import os
import pandas as pd
from sheets_api.spreadsheetsFunctions import appendCells
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#Take environment variables from .env
load_dotenv()

path = os.getenv("DRIVER_PATH")

options = Options()
options.headless = True

service = Service(executable_path=str(path))
driver = webdriver.Chrome(service=service, options=options)
#nameList = []
#hashList = []
animeData = []

website = 'https://nyaa.si/user/puyero?p=1'
driver.get(website)

trList = driver.find_elements(by = "xpath", value='//tbody/tr')

for line in trList:

    title = line.find_element(by="xpath", value='./td[@colspan="2"]/a[not(@class="comments")]')
    link = line.find_elements(by="xpath", value='./td[@class="text-center"]/a')

    #nameList.append(title.text)
    #hashList.append(link[1].get_attribute("href")[20:60])

    animeData.append({"tittle" : title.text, "hash" : link[1].get_attribute("href")[20:60]})


appendCells(animeData)


driver.quit()



