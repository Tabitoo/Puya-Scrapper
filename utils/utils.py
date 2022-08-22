
def filterData(rangeData: list, animeTitle: str) -> bool:

    finalResult = False

    for data in rangeData:
        if data[0] == animeTitle:
            finalResult = True
            break

    return finalResult
