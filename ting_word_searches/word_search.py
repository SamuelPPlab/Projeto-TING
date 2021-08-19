def exists_word(word, instance):
    resultList = []
    for indexFile in range(len(instance)):
        fileInPosition = instance.search(indexFile)
        searchResult = {
            "palavra": word,
            "arquivo": fileInPosition,
            "ocorrencias": [],
        }

        for indexLine, line in enumerate(fileInPosition["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                searchResult["ocorrencias"].append({"linha": indexLine + 1})
            if len(searchResult["ocorrencias"]) > 0:
                resultList.append(searchResult)
    return resultList


def search_by_word(word, instance):
    resultList = []
    for indexFile in range(len(instance)):
        fileInPosition = instance.search(indexFile)
        searchResult = {
            "palavra": word,
            "arquivo": fileInPosition,
            "ocorrencias": [],
        }

        for indexLine, line in enumerate(fileInPosition["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                searchResult["ocorrencias"].append({"linha": indexLine + 1})
            if len(searchResult["ocorrencias"]) > 0:
                resultList.append(searchResult)
    return resultList
