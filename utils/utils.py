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

def compare_names(puya_name: list, kitsu_name: list, len_name: int) -> bool:

    equals_points = 0

    for index, word in enumerate(kitsu_name):
        if word == puya_name[index]:
            equals_points = equals_points + 1

    if equals_points == len_name:
        return True  
    else:
        return False



