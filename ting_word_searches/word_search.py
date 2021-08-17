def exists_word(word, instance):
    list = []
    for index in range(len(instance)):
        file = instance.search(index)
        searched_words = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                searched_words["ocorrencias"].append({'linha': index + 1})
            if len(searched_words["ocorrencias"]):
                list.append(searched_words)

    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
