from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    list_return = list()
    for doc in instance._data:
        flag = False
        equal = []
        phrase = doc["linhas_do_arquivo"]
        for index, line in enumerate(phrase):
            if word.lower() in line.lower().strip(".,"):
                equal.append({"linha": index + 1})
                flag = True
        if flag is True:
            list_return.append(
                {
                    "palavra": word,
                    "arquivo": doc["nome_do_arquivo"],
                    "ocorrencias": equal,
                }
            )

    return list_return


def search_by_word(word, instance):
    list_return = list()
    for doc in instance._data:
        flag = False
        equal = []
        phrase = doc["linhas_do_arquivo"]
        for index, line in enumerate(phrase):
            if word.lower() in line.lower().strip(".,"):
                equal.append({"linha": index + 1, "conteudo": line})
                flag = True
        if flag is True:
            list_return.append(
                {
                    "palavra": word,
                    "arquivo": doc["nome_do_arquivo"],
                    "ocorrencias": equal,
                }
            )

    return list_return


if __name__ == "__main__":
    project = Queue()
    process(
        "../statics/novo_paradigma_globalizado-min.txt",
        project,
    )
    process(
        "../statics/nome_pedro.txt",
        project,
    )
    word = search_by_word("sobre", project)

    # [
    #    {
    #        "palavra": "sobre",
    #        "arquivo": "../statics/novo_paradigma_globalizado-min.txt",
    #        "ocorrencias": [{"linha": 17}, {"linha": 18}],
    #    },
    #    {
    #        "palavra": "sobre",
    #        "arquivo": "../statics/nome_pedro.txt",
    #        "ocorrencias": [{"linha": 1}],
    #    },
    # ]
