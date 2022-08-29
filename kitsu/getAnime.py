import requests
from utils.utils import filter_puya_name, convert_split_name, compare_names, get_chapter

def getByName(animeTitle: str):

    #Usar el metodo split para separar el nombre de un anime y los datos que pone puyasub en el titulo
    #Quitar las ultimas tres posiciones del array que retorna el split,

    equals_name_validation = False
    kitsu_id = "null"

    newName = filter_puya_name(animeTitle)

    splitName = newName.split(" ")

    convert_name = convert_split_name(splitName)

    puya_len_name = len(convert_name)
    
    response = requests.get(f'https://kitsu.io/api/edge/anime?filter[text]={newName}')

    animeData = response.json().get('data')

    for anime in animeData:

        kitsuName_en_jp = anime.get('attributes').get('titles').get("en_jp") 
        kitsuName_en = anime.get('attributes').get('titles').get("en")
        
        if kitsuName_en_jp and kitsuName_en is None:
            break

        if kitsuName_en_jp is None:
            kitsuName_en_jp = "null"

        if kitsuName_en is None:
            kitsuName_en = "null"
            print(f'kitsuName_en desde el elif: {kitsuName_en}')

        print(f'kitsuName_en desde fuera del elif: {kitsuName_en}')
        print(f'k1tsuName_en_jp desde fuera del elif: {kitsuName_en_jp}')

        kitsuSplitName_en_jp = kitsuName_en_jp.split(" ")

        kitsuSplitName_en_jp = convert_split_name(kitsuSplitName_en_jp)

        kitsuSplitName_en = kitsuName_en.split(" ")

        kitsuSplitName_en = convert_split_name(kitsuSplitName_en)

        kitsu_len_name_en_jp = len(kitsuSplitName_en_jp)
        kitsu_len_name_en = len(kitsuSplitName_en)

        if not kitsu_len_name_en_jp == puya_len_name and kitsu_len_name_en == puya_len_name:
            continue 

        equals_name_validation = compare_names(convert_name, kitsuSplitName_en_jp, kitsuSplitName_en, puya_len_name)

        if equals_name_validation:
            kitsu_id = anime.get('id')
            break

    return kitsu_id

def getById(id) -> dict:

    pass
