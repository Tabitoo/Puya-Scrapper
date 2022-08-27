import requests
from utils.utils import filter_puya_name, convert_split_name, compare_names

def getByName(name: str):

    #Usar el metodo split para separar el nombre de un anime y los datos que pone puyasub en el titulo
    #Quitar las ultimas tres posiciones del array que retorna el split,

    equals_name_validation = False
    kitsu_id = "null"

    newName = filter_puya_name("[PuyaSubs!] Yowai 5000-nen no Soushoku Dragon - Iwarenaki Jaryuu Nintei - 05 [ESP-ENG][720p][84DACA8F].mkv")
    
    splitName = newName.split(" ")

    convert_name = convert_split_name(splitName)

    puya_len_name = len(convert_name)
    
    response = requests.get(f'https://kitsu.io/api/edge/anime?filter[text]={newName}')

    animeData = response.json().get('data')

    for anime in animeData:

        kitsuName = anime.get('attributes').get('titles').get("en_jp")

        kitsuSplitName = kitsuName.split(" ")

        kitsuSplitName = convert_split_name(kitsuSplitName)

        kitsu_len_name = len(kitsuSplitName)

        if not kitsu_len_name == puya_len_name:
            continue 

        equals_name_validation = compare_names(convert_name, kitsuSplitName, puya_len_name)

        if equals_name_validation:
            kitsu_id = anime.get('id')
            break

    print(kitsu_id)

def getById(id) -> dict:

    pass
