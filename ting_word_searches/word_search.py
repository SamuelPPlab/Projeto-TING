from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    words = []
    length = instance.__len__()

    for i in range(length):
        position = instance.search(i)
        result = {
            "palavra": word,
            "arquivo": position,
            "ocorrencias": [],
        }
        for index, line in enumerate(position["linhas_do_arquivo"]):
            if len(result["ocorrencias"]) > 0:
                words.append(result)

            if word.lower() in line.lower():
                result["ocorrencias"].append({"linha": index + 1})
    return words


def search_by_word(word, instance):
    result = exists_word(word, instance)
    if result:
        for index, line in enumerate(txt_importer(instance.search(0))):
            if index == result[0]["ocorrencias"][index]["linha"] - 1:
                result[0]["ocorrencias"][index]["conteudo"] = line
    return result
