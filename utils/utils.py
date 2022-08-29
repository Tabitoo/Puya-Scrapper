def filterData(rangeData: list, animeTitle: str) -> bool:

    finalResult = False

    for data in rangeData:
        if data[0] == animeTitle:
            finalResult = True
            break

    return finalResult

def filter_puya_name(name: str) -> str:
    
    nameList = name.split(" ")

    total = len(nameList)
    newList = nameList[1:total - 3]
    newStr = " ".join(newList)

    print(newStr)

    return newStr


def convert_split_name(name: list):

    for index, word in enumerate(name):
        
        indice_coma = word.find(",")

        indice_punto = word.find(":")

        if word == "-":
            name.pop(index)
        
        if indice_coma != -1:
            name[index] = word[:indice_coma] 

        if indice_punto != -1:
            name[index] = word[:indice_punto]

    return name

def compare_names(puya_name: list, kitsu_name_en_jp: list, kitsu_name_en: list, len_name: int) -> bool:

    equals_points_en_jp = 0
    equals_points_en = 0

    if len_name == len(kitsu_name_en_jp):
        for index, word in enumerate(kitsu_name_en_jp):
            if word == puya_name[index]:
                equals_points_en_jp = equals_points_en_jp + 1

    if len_name == len(kitsu_name_en):
        for index, word in enumerate(kitsu_name_en):
            if word == puya_name[index]:
                equals_points_en = equals_points_en + 1

    if equals_points_en_jp == len_name or equals_points_en == len_name:
        return True
    else:
        return False

def get_chapter(name: str):
    
    nameList = name.split(" ")

    total = len(nameList)

    chapter = nameList[total - 2]

    chapter = int(chapter)

    chapter = str(chapter)

    return chapter




