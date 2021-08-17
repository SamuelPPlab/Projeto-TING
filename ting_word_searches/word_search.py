def exists_word(word, instance):
    list_files = []

    for index in range(len(instance)):
        file = instance.search(index)
        result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {
                    "linha": (file["linhas_do_arquivo"].index(line) + 1)
                    for line in file["linhas_do_arquivo"]
                    if word.lower() in line.lower()
                }
            ],
        }

        if result["ocorrencias"] == [{}]:
            pass
        else:
            list_files.append(result)

    return list_files


def search_by_word(word, instance):
    list_files = []

    for index in range(len(instance)):
        file = instance.search(index)
        result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {
                    "linha": (file["linhas_do_arquivo"].index(line) + 1),
                    "conteudo": line,
                }
                for line in file["linhas_do_arquivo"]
                if word.lower() in line.lower()
            ],
        }

        if result["ocorrencias"] == []:
            list_files = []
        else:
            list_files.append(result)

    return list_files
