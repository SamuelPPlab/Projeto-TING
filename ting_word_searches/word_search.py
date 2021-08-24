def exists_word(word, instance):
    """Aqui irá sua implementação"""


def search_by_word(word, instance):
    response = []
    for n in range(len(instance)):
        element = instance.search(n)
        dict_response = {
            "palavra": word,
            "arquivo": element["nome_do_arquivo"],
            "ocorrencias": []
        }
        for line in element["linhas_do_arquivo"]:
            index_word = (line.lower()).find(word.lower())
            if index_word != -1:
                ocorrencia = {
                    "linha": n + 1,
                    "conteudo": line
                }
                dict_response["ocorrencias"].append(ocorrencia)
    if len(dict_response["ocorrencias"]) == 0:
        return []
    response.append(dict_response)
    return response

# lower https://github.com/tryber/sd-07-project-ting/pull/74/files
