# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process


def exists_word(word, instance):
    data = instance.__iter__()
    ocorrencias = []
    file_name = ''
    for item in data:
        file_name = item['nome_do_arquivo']
        for row, key in zip(item['linhas_do_arquivo'], range(1, len(item)+1)):
            row = row.lower()
            if word.lower() in row:
                ocorrencias.append({"linha": key})

    result = [
        {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": ocorrencias
        }
    ]
    if len(ocorrencias) == 0:
        return []
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# if __name__ == "__main__":
#     queue = Queue()
#     data = queue.__iter__()
#     # path = "statics/arquivo_teste.txt"
#     # result = process(path, queue)
#     # path = "statics/nome_pedro.txt"
#     # result = process(path, queue)
#     path = "statics/novo_paradigma_globalizado-min.txt"
#     result = process(path, queue)
#     # path = "statics/novo_paradigma_globalizado.txt"
#     # result = process(path, queue)
#     exists_word('aprovar', queue)
