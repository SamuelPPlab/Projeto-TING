def exists_word(word, instance):
    search_result = []
    for file in range(instance.__len__()):
        result = {
            "palavra": word,
            "arquivo": instance.search(file)["nome_do_arquivo"],
            "ocorrencias": [],
        }
        file_lines = instance.search(file)["linhas_do_arquivo"]
        for index, line in enumerate(file_lines):
            if word.lower() in line.lower():
                result["ocorrencias"].append({"linha": index + 1})

        if result["ocorrencias"].__len__() != 0:
            search_result.append(result)

    return search_result


def search_by_word(word, instance):
    search_result = []
    for file in range(instance.__len__()):
        result = {
            "palavra": word,
            "arquivo": instance.search(file)["nome_do_arquivo"],
            "ocorrencias": [],
        }
        file_lines = instance.search(file)["linhas_do_arquivo"]
        for index, line in enumerate(file_lines):
            if word.lower() in line.lower():
                result["ocorrencias"].append(
                    {
                        "linha": index + 1,
                        "conteudo": line,
                    }
                )

        if result["ocorrencias"].__len__() != 0:
            search_result.append(result)

    return search_result
