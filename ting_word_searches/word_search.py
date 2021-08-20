def exists_word(word, instance):
    data = list()
    for index in range(len(instance)):
        file_path = instance.search(index)
        file_data = {
            "palavra": word,
            "arquivo": file_path["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for row in file_path["linhas_do_arquivo"]:
            if word.lower() in row.lower():
                file_data["ocorrencias"].append({"linha": index + 1})

        if len(file_data["ocorrencias"]) > 0:
            data.append(file_data)
            print(file_data)
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
