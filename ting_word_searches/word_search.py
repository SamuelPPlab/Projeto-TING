
def exists_word(word, instance):
    array = []
    counter = 0
    for element in instance._data:
        obj = {
            "palavra": word,
            "arquivo": element["nome_do_arquivo"],
            "ocorrencias": []
        }
        for _index, line in enumerate(element["linhas_do_arquivo"]):
            if word in line:
                counter += 1
                obj["ocorrencias"].append({"linha": counter})
                array.append(obj)
    return array


def search_by_word(word, instance):
    array = []
    for element in instance._data:
        obj = {
            "palavra": word,
            "arquivo": element["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index, line in enumerate(element["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                obj["ocorrencias"].append({"linha": index+1, "conteudo": line})
                array.append(obj)
    return array
