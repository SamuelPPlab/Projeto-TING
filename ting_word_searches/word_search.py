import re


def exists_word(word, instance):
    result = []
    for file_data in instance._queue:
        occurrences = []
        for index, line in enumerate(file_data["linhas_do_arquivo"]):
            if re.search(word, line, re.IGNORECASE):
                occurrences.append({"linha": index + 1})

        if occurrences != []:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result


def search_by_word(word, instance):
    result = []
    for file_data in instance._queue:
        occurrences = []
        for index, line in enumerate(file_data["linhas_do_arquivo"]):
            if re.search(word, line, re.IGNORECASE):
                occurrences.append({
                    "linha": index + 1,
                    "conteudo": line,
                    })

        if occurrences != []:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result
