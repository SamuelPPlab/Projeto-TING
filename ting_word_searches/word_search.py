def exists_word(word, instance):
    format_text_line = [{"palavra": word, "arquivo": "", "ocorrencias": []}]

    for item in range(len(instance)):
        file = instance.search(item)
        format_text_line[0]["arquivo"] = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        number_of_occurence = format_text_line[0]["ocorrencias"]

        for index, line in enumerate(lines):
            if word in line:
                number_of_occurence.append({"linha": index + 1})

        ocurrences = len(number_of_occurence)
        if ocurrences > 0:
            return format_text_line
    return []


def search_by_word(word, instance):
    format_text_line = [{"palavra": word, "arquivo": "", "ocorrencias": []}]

    for item in range(len(instance)):
        file = instance.search(item)
        format_text_line[0]["arquivo"] = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        number_of_occurence = format_text_line[0]["ocorrencias"]

        for index, line in enumerate(lines):
            if word in line:
                number_of_occurence.append(
                    {"linha": index + 1, "conteudo": line}
                )

        ocurrences = len(number_of_occurence)
        if ocurrences > 0:
            return format_text_line
    return []
