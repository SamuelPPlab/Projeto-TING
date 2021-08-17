def exists_word(word, instance):
    return build_result_list(word, instance, "simple")


def search_by_word(word, instance):
    return build_result_list(word, instance, "complete")


def build_result_list(word, instance, type):
    result_list = []
    for index in range(instance.size()):
        content_processed = instance.search(index)
        occurrences = get_occurrences_by_word(
            word, content_processed["linhas_do_arquivo"], type
        )
        if len(occurrences):
            result_list.append(
                {
                    "palavra": word,
                    "arquivo": content_processed["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result_list


def get_occurrences_by_word(word, lines, type="simple"):
    if type == "simple":
        return [
            {"linha": line_number + 1}
            for line_number, line in enumerate(lines)
            if word.upper() in line.upper()
        ]
    elif type == "complete":
        return [
            {"linha": line_number + 1, "conteudo": line}
            for line_number, line in enumerate(lines)
            if word.upper() in line.upper()
        ]
    else:
        return None
