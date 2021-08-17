def exists_word(word, instance):
    get_word = []
    for index in range(len(instance)):
        find_file = instance.search(index)
        find_lines = find_file["linhas_do_arquivo"]
        ocurrences = []
        line_oc = 0
        for line in find_lines:
            line_oc += 1
            if word in line:
                ocurrences.append({"linha": line_oc})
        if len(ocurrences) > 0:
            get_word.append(
                {
                    "palavra": word,
                    "arquivo": find_file["nome_do_arquivo"],
                    "ocorrencias": ocurrences,
                }
            )
    return get_word                


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
