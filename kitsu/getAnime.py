import requests
from utils.utils import filter_puya_name

def getByName(name: str):

    #Usar el metodo split para separar el nombre de un anime y los datos que pone puyasub en el titulo
    #Quitar las ultimas tres posiciones del array que retorna el split,

    newName = filter_puya_name("[PuyaSubs!] Yowai 5000-nen no Soushoku Dragon - Iwarenaki Jaryuu Nintei - 05 [ESP-ENG][720p][84DACA8F].mkv")
    
    splitName = newName.split(" ")

    response = requests.get(f'https://kitsu.io/api/edge/anime?filter[text]={newName}')

    animeData = response.json().get('data')


    for anime in animeData:

        kitsuName = anime.get('attributes').get('titles').get("en_jp")

        kitsuSplitName = kitsuName.split(" ")

        


    print(response.json().get('data')[0].get('attributes').get('titles'))
    

def getById(id) -> dict:

    pass
