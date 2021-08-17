def exists_word(word, instance):
    """Aqui irá sua implementação"""

    queue = instance._data
    for item in queue:
        ocorruncies = []
        result_obj = {"palavra": word, "arquivo": item["nome_do_arquivo"]}
        file_lines = item["linhas_do_arquivo"]
        for index, line in enumerate(file_lines):
            if word in line:
                ocorruncies.append({"linha": index + 1})
    result_obj["ocorrencias"] = ocorruncies
    if len(ocorruncies) == 0:
        return []
    final_result = [result_obj]

    return final_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    queue = instance._data
    for item in queue:
        ocorruncies = []
        result_obj = {"palavra": word, "arquivo": item["nome_do_arquivo"]}
        file_lines = item["linhas_do_arquivo"]
        for index, line in enumerate(file_lines):
            if word.lower() in line.lower():
                ocorruncies.append({"linha": index + 1, "conteudo": line})
    result_obj["ocorrencias"] = ocorruncies
    if len(ocorruncies) == 0:
        return []
    final_result = [result_obj]

    return final_result
