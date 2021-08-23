def exists_word(word, instance):
    results = []
    for i in range(len(instance)):
        posicao = instance.search(i)
        print("-----------------", posicao)
        resultadoDaBusca = {
            "palavra": word,
            "arquivo": posicao["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for posicaoDaLinha, linha in enumerate(posicao["linhas_do_arquivo"]):
            if word.lower() in linha.lower():
                resultadoDaBusca["ocorrencias"].append(
                    {"linha": posicaoDaLinha + 1}
                )
            if len(resultadoDaBusca["ocorrencias"]) > 0:
                results.append(resultadoDaBusca)

    return results


def search_by_word(word, instance):
    """Return the lines with the content where the word exists"""
