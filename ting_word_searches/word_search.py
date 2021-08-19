def exists_word(word, instance):
    files = list()
    for index in range(len(instance)):
        file = instance.search(index)

        word_found = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list()
        }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_found["ocorrencias"].append({
                    "linha": index + 1
                })
            if len(word_found["ocorrencias"]) > 0:
                files.append(word_found)
    return files


def search_by_word(word, instance):
    files = list()
    for index in range(len(instance)):
        file = instance.search(index)

        word_found = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list(),
        }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_found["ocorrencias"].append({
                    "linha": index + 1,
                    "conteudo": line
                })
            if len(word_found["ocorrencias"]) > 0:
                files.append(word_found)
    return files
