def get_ocurrences(data, word, with_content):
    element = {
        "palavra": word,
        "arquivo": data["nome_do_arquivo"],
        "ocorrencias": []
    }
    for index, line in enumerate(data["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            element["ocorrencias"].append({"linha": index + 1})
            if with_content:
                element["ocorrencias"][index]["conteudo"] = line
    return element


def exists_word(word, instance):
    result = list()
    for sample in instance._queue:
        element = get_ocurrences(sample, word, 0)
        if len(element["ocorrencias"]) > 0:
            result.append(element)
    return result


def search_by_word(word, instance):
    result = list()
    for sample in instance._queue:
        element = get_ocurrences(sample, word, 1)
        if len(element["ocorrencias"]) > 0:
            result.append(element)
    return result
