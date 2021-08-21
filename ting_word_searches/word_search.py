def exists_word(word, instance):
    index = 0
    exists = []

    while index < instance.__len__():
        file = instance.search(index)
        content = file["linhas_do_arquivo"]
        exists_in_file = {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": []
        }
        for line in content:
            if word.lower() in line.lower():
                exists_in_file["ocorrencias"].append({"linha": index + 1})
        if len(exists_in_file["ocorrencias"]):
            exists.append(exists_in_file)
        index += 1
    return exists


def search_by_word(word, instance):
    index = 0
    exists = []

    while index < instance.__len__():
        file = instance.search(index)
        content = file["linhas_do_arquivo"]
        exists_in_file = {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": []
        }
        for line in content:
            if word.lower() in line.lower():
                exists_in_file["ocorrencias"].append({
                    "linha": index + 1,
                    "conteudo": line
                })
        if len(exists_in_file["ocorrencias"]):
            exists.append(exists_in_file)
        index += 1
    return exists
