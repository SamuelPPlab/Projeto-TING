def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        file = instance.search(index)
        count = []
        for value in file["linhas_do_arquivo"]:
            if word.lower() in value.lower():
                count.append(
                  {"linha": file["linhas_do_arquivo"].index(value) + 1})
        if len(count) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": count,
                }
            )
    return result


def search_by_word(word, instance):
    result = []
    for index in range(len(instance)):
        file = instance.search(index)
        count = []
        for value in file["linhas_do_arquivo"]:
            if word.lower() in value.lower():
                count.append(
                  {"linha": file["linhas_do_arquivo"].index(value) + 1,
                   "conteudo": value})
        if len(count) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": count,
                }
            )
    return result
