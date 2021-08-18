# Ref: Feito no plantão do Moisés Santana

def exists_word(word, instance):
    """
        - pesquisa palavra dentro de linhas_do_arquivo
        - Retorna um objeto com as chaves:
            - A palavra: word
            - Nome do arquivo: nome_do_arquivo
            - Ocorrencias: lista de dicts com "[linha]: número_da_linha"
        - Retorna lista vazia se não houver result
    """
    word_exists = list()
    for index in range(instance.__len__()):
        ocorrencias = list()
        file = instance.search(index)
        for line in file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                ocorrencias.append(
                    {"linha": file["linhas_do_arquivo"].index(line) + 1}
                )
        if len(ocorrencias) != 0:
            dict_ = {
                "arquivo": file["nome_do_arquivo"],
                "palavra": word,
                "ocorrencias": ocorrencias
            }
            word_exists.append(dict_)
    return word_exists


def search_by_word(word, instance):
    """
        - pesquisa palavra dentro de linhas_do_arquivo
        - Retorna um objeto com as chaves:
            - A palavra: word
            - Nome do arquivo: nome_do_arquivo
            - Ocorrencias:
                - Lista de dicts com "[linha]: número_da_linha"
                - ["conteudo"]: conteudo_da_linha
        - Retorna lista vazia se não houver resultado
    """
    word_exists = list()
    for index in range(instance.__len__()):
        ocorrencias = list()
        file = instance.search(index)
        for line in file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                ocorrencias.append(
                    {
                        "linha": file["linhas_do_arquivo"].index(line) + 1,
                        "conteudo": line
                    }
                )
        if len(ocorrencias) != 0:
            dict_ = {
                "arquivo": file["nome_do_arquivo"],
                "palavra": word,
                "ocorrencias": ocorrencias
            }
            word_exists.append(dict_)
    return word_exists
