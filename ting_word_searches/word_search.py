def exists_word(word, instance):
    my_dict = {
        "palavra": word,
        "arquivo": "",
        "ocorrencias": [],
    }

    for i in range(len(instance)):
        file = instance.search(i)
        print(f"********{file}")
        my_dict["arquivo"] = file["nome_do_arquivo"]

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word in line:
                my_dict["ocorrencias"].append({"linha": index + 1})
        if len(my_dict["ocorrencias"]) == 0:
            return []
    return [my_dict]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
