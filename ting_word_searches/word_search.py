def search_words_and_exists(word, instance, byWord=False):
    result = []
    for i in range(len(instance)):
        file_searched = instance.search(i)
        result.append(
            {
                "palavra": word,
                "arquivo": file_searched["nome_do_arquivo"],
                "ocorrencias": [],
            }
        )
        lines = file_searched["linhas_do_arquivo"]
        occurrence = result[0]["ocorrencias"]

    for i, line in enumerate(lines):
        if byWord:
            if word.upper() in line.upper():
                occurrence.append({"linha": i + 1, "conteudo": line})
        else:
            if word in line:
                occurrence.append({"linha": i + 1})

    if not len(occurrence):
        return []
    return result


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    return search_words_and_exists(word, instance)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    return search_words_and_exists(word, instance, True)
