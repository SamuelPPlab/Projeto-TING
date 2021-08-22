def exists_word(word, instance):
    results = []
    for i in range(len(instance)):
        posicao = instance.search(i)
        resultadoDaBusca = {
            "palavra": word,
            "arquivo": posicao,
            "ocorrencias": [],
        }

        for posicaoDaLinha, linha in enumerate(posicao["linhas_do_arquivo"]):
            if len(resultadoDaBusca["ocorrencias"]) > 0:
                results.append(resultadoDaBusca)

            if word.lower() in linha.lower():
                resultadoDaBusca["ocorrencias"].append(
                    {"linha": posicaoDaLinha + 1}
                )

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
