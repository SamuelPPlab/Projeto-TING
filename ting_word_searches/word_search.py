def exists_word(word, instance):
    result = []
    occurrence = {
        "palavra": word,
        "arquivo": [],
        "ocorrencias": []
    }

    for item in range(len(instance)):
        word_exist = instance.search(item)
        occurrence["arquivo"] = word_exist["nome_do_arquivo"]
        # print(occurrence)
        for index, line in enumerate(word_exist["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrence["ocorrencias"].append({"linha": index + 1})
            if len(occurrence["ocorrencias"]):
                result.append(occurrence)
    return result

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
