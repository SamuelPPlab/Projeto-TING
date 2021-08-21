def exists_word(word, instance):
    for item in range(0, instance.__len__()):
        line = search_line(word, instance, item)

    if line == []:
        return []

    result = [
        {
            "palavra": word,
            "arquivo": instance.search(item)["nome_do_arquivo"],
            "ocorrencias": [{"linha": line}],
        }
    ]
    return result


def search_by_word(word, instance):
    for item in range(0, instance.__len__()):
        result = search_content(word, instance, item)

    if result == []:
        return []

    result = [
        {
            "palavra": word,
            "arquivo": instance.search(item)["nome_do_arquivo"],
            "ocorrencias": result,
        }
    ]
    return result


def search_line(word, instance, item):
    lists = []
    line = 0
    for index in instance.search(item)["linhas_do_arquivo"]:
        result_in_lowercase = index.lower().find(word.lower())
        if result_in_lowercase >= 0:
            line += 1
            lists.append(result_in_lowercase)
        else:
            return lists
    return line


def search_content(word, instance, item):
    lists = []
    line = 0
    for index in instance.search(item)["linhas_do_arquivo"]:
        result_in_lowercase = index.lower().find(word.lower())
        if result_in_lowercase >= 0:
            line += 1
            lists.append({"linha": line, "conteudo": index})
        else:
            return lists

    return lists


# Source: Anderson Alves / Emerson Junqueira
