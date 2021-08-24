def insert_content(index, line, type):
    add_dict = dict({"linha": index + 1})
    if type != "exists_word":
        add_dict["conteudo"] = line

    return add_dict


def find_word(word, instance, type="exists_word"):
    message = list()
    for data_list in instance.convertToList():
        dic = dict(
            {
                "palavra": word,
                "arquivo": data_list["nome_do_arquivo"],
                "ocorrencias": [],
            }
        )
        for index, line in enumerate(data_list["linhas_do_arquivo"]):
            add_dict = insert_content(index, line, type)

            if word.lower() in line.lower():
                dic["ocorrencias"].append(add_dict)

        if dic["ocorrencias"]:
            message.append(dic)

    return message


def exists_word(word, instance):
    return find_word(word, instance)


def search_by_word(word, instance):
    return find_word(word, instance, "search_by_word")
