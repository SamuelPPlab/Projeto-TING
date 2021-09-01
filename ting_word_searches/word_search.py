def exists_word(word, instance):
    list_return = list()
    for doc in instance._data:
        flag = False
        equal = []
        phrase = doc["linhas_do_arquivo"]
        for index, line in enumerate(phrase):
            if word.lower() in line.lower().strip(".,"):
                equal.append({"linha": index + 1})
                flag = True
        if flag is True:
            list_return.append(
                {
                    "palavra": word,
                    "arquivo": doc["nome_do_arquivo"],
                    "ocorrencias": equal,
                }
            )

    return list_return


def search_by_word(word, instance):
    list_return = list()
    for doc in instance._data:
        flag = False
        equal = []
        phrase = doc["linhas_do_arquivo"]
        for index, line in enumerate(phrase):
            if word.lower() in line.lower().strip(".,"):
                equal.append({"linha": index + 1, "conteudo": line})
                flag = True
        if flag is True:
            list_return.append(
                {
                    "palavra": word,
                    "arquivo": doc["nome_do_arquivo"],
                    "ocorrencias": equal,
                }
            )

    return list_return
