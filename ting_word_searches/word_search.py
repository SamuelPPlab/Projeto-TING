def exists_word(word, instance):
    """Aqui irá sua implementação"""
    list_return = list()
    for file in instance._data:
        target = False
        equal = []
        phrase = file["linhas_do_arquivo"]
        for index, line in enumerate(phrase):
            if word.lower() in line.lower().strip(".,"):
                equal.append({"linha": index + 1})
                target = True
        if target is True:
            list_return.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": equal,
                }
            )

    return list_return


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    list_word = []
    for index in range(len(instance)):
        file = instance.search(index)
        file_name = file["nome_do_arquivo"]
        file_lines = file["linhas_do_arquivo"]
        list_on_file = []

        for line_index, line in enumerate(file_lines):
            if word.lower() in line.lower():
                list_on_file.append(
                    {"linha": line_index + 1, "conteudo": line}
                )

        if len(list_on_file) != 0:
            list_word.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": list_on_file,
                }
            )

    return list_word
