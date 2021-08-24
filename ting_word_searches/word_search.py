def exists_word(word, instance):
    """Aqui irá sua implementação"""
    list = []
    item_length = instance.__len__()
    for item in range(0, item_length):
        content = instance.search(item)["linhas_do_arquivo"]
        result = frequency_in_line(word, content)
    if result != []:
        file_name = instance.search(item)["nome_do_arquivo"]
        list.append({
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": result,
        })
    else:
        return []

    return list


def frequency_in_line(word, content):
    list = []
    for index, line in enumerate(content):
        index += 1
        returned_word = line.upper().find(word.upper())
        if returned_word > 0:
            list.append({"linha": index})

    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
