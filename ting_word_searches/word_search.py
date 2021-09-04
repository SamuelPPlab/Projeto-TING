def exists_word(word, instance):
    result = list()
    for index in range(len(instance)):
        file = instance.search(index)

        new_obj = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list()
        }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                new_obj["ocorrencias"].append({
                    "linha": index + 1
                })
            if len(new_obj["ocorrencias"]) > 0:
                result.append(new_obj)
    return result


def search_by_word(word, instance):
    result = list()
    for index in range(len(instance)):
        file = instance.search(index)

        new_obj = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list(),
        }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                new_obj["ocorrencias"].append({
                    "linha": index + 1,
                    "conteudo": line
                })
            if len(new_obj["ocorrencias"]) > 0:
                result.append(new_obj)
    return result
