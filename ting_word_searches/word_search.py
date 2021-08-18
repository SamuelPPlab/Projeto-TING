def exists_word(word, instance):
    word_original = word
    word = word.lower()
    result = list()
    ocorrencias = list()
    files = instance.get()
    for file in files:
        linhas = file["linhas_do_arquivo"]
        arquivo = file["nome_do_arquivo"]
        conta_linhas = 0
        for linha in linhas:
            linha = linha.replace(".", "")
            linha = linha.lower()
            palavras = linha.split(" ")
            conta_linhas += 1
            if word in palavras:
                ocorrencias.append({"linha": conta_linhas})
        result.append(
            {
                "palavra": word_original,
                "arquivo": arquivo,
                "ocorrencias": ocorrencias,
            }
        )
        if len(ocorrencias) == 0:
            return []
    return result


def search_by_word(word, instance):
    word = word.lower()
    result = list()
    ocorrencias = list()
    files = instance.get()
    for file in files:
        linhas = file["linhas_do_arquivo"]
        arquivo = file["nome_do_arquivo"]
        conta_linhas = 0
        for linha in linhas:
            linha_original = linha
            linha = linha.replace(".", "")
            linha = linha.lower()
            palavras = linha.split(" ")
            conta_linhas += 1
            if word in palavras:
                ocorrencias.append(
                    {"linha": conta_linhas, "conteudo": linha_original}
                )
        result.append(
            {"palavra": word, "arquivo": arquivo, "ocorrencias": ocorrencias}
        )
        if len(ocorrencias) == 0:
            return []
    return result
