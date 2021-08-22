def get_ocurrences(data, word):
    element = {
        "palavra": word,
        "arquivo": data["nome_do_arquivo"],
        "ocorrencias": []
    }
    for index, line in enumerate(data["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            element["ocorrencias"].append({"linha": index + 1})
    return element


def exists_word(word, instance):
    result = list()
    for sample in instance._queue:
        element = get_ocurrences(sample, word)
        if len(element["ocorrencias"]) > 0:
            result.append(element)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
