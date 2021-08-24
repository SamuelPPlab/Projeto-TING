def exists_word(word, instance):
    """Aqui irá sua implementação"""
    format_list = [{"palavra": word, "arquivo": "", "ocorrencias": []}]
    for item in range(len(instance)):
        file = instance.search(item)
        format_list[0]["arquivo"] = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        times = format_list[0]["ocorrencias"]

        for position, line in enumerate(lines):
            if word.lower() in line.lower():
                times.append({"linha": position + 1})

        ocurrences = len(times)
        if ocurrences > 0:
            return format_list
    return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    format_list = [{"palavra": word, "arquivo": "", "ocorrencias": []}]
    for item in range(len(instance)):
        file = instance.search(item)
        format_list[0]["arquivo"] = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        times = format_list[0]["ocorrencias"]

        for position, line in enumerate(lines):
            if word.lower() in line.lower():
                times.append({"linha": position + 1, "conteudo": line})

        ocurrences = len(times)
        if ocurrences > 0:
            return format_list
    return []
