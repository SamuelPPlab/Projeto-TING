def exists_word(word, instance):
    result = [{"palavra": word, "arquivo": "", "ocorrencias": []}]
    for item in range(len(instance)):
        file = instance.search(item)
        result[0]["arquivo"] = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        occurrence = result[0]["ocorrencias"]

        for index, line in enumerate(lines):
            if word in line:
                occurrence.append({"linha": index + 1})

        if len(occurrence) > 0:
            return result
    return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
