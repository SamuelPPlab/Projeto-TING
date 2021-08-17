from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    result = []

    files_names = instance.data_names()
    for names in files_names:
        for file in txt_importer(names):
            words = list(map(lambda x: x["palavra"], result))
            if word in file and word not in words:
                info = {
                    "palavra": word,
                    "arquivo": names,
                    "ocorrencias": [
                        {"linha": txt_importer(names).index(file) + 1}
                    ],
                }
                result.append(info)
            elif word in file:
                result[0]["ocorrencias"].append(
                    {"linha": txt_importer(names).index(file) + 1}
                )

    return result


def search_by_word(word, instance):
    result = []

    files_names = instance.data_names()
    for names in files_names:
        for file in txt_importer(names):
            words = list(map(lambda x: x["palavra"], result))
            if word.lower() in file.lower() and word not in words:
                info = {
                    "palavra": word,
                    "arquivo": names,
                    "ocorrencias": [
                        {
                            "linha": txt_importer(names).index(file) + 1,
                            "conteudo": file,
                        }
                    ],
                }
                result.append(info)
            elif word.lower() in file.lower():
                result[0]["ocorrencias"].append(
                    {
                        "linha": txt_importer(names).index(file) + 1,
                        "conteudo": file,
                    }
                )

    return result
