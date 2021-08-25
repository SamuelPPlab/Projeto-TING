def exists_word(word, instance):
    """Aqui irá sua implementação"""
    new_list = list()
    for i in range(len(instance)):
        file = instance.search(i)

        find_word = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list()
        }

        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                find_word["ocorrencias"].append({
                    "linha": i + 1
                })
            if len(find_word["ocorrencias"]) > 0:
                new_list.append(find_word)
    return new_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
