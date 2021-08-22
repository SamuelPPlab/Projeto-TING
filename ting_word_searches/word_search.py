def exists_word(word, instance):
    files = []

    for index in range(instance.__len__()):
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

        if result["ocorrencias"] != [{}]:
            files.append(result)

    return files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
