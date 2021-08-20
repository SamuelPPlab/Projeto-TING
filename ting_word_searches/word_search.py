def exists_word(word, instance):
    for file in range(len(instance)):
        data = instance.search(file)["linhas_do_arquivo"]
        dicionario = find_word(word, data, instance, file, False)
    return dicionario


def find_word(word, data, instance, file, complete):
    dicionario = []
    acc = 0
    lista = []
    for linha in data:
        acc += 1
        caseInsensitive = linha.lower().find(word.lower())
        if caseInsensitive >= 0:
            if complete:
                lista.append({"linha": acc, "conteudo": linha})
            else:
                lista.append({"linha": acc})
        else:
            return lista
    dicionario.append(
        {
            "palavra": word,
            "arquivo": instance.search(file)["nome_do_arquivo"],
            "ocorrencias": lista,
        }
    )
    return dicionario


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
