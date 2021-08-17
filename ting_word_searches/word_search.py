def exists_word(word, instance):
    result_list = []
    for index in range(instance.size()):
        content_processed = instance.search(index)
        occurrences = [
            {"linha": line_number + 1}
            for line_number, line in enumerate(
                content_processed["linhas_do_arquivo"]
            )
            if word in line
        ]

        if len(occurrences):
            result_list.append(
                {
                    "palavra": word,
                    "arquivo": content_processed["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
