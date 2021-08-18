# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process
# import re


def exists_word(word, instance):
    result = list()
    ocorrencias = list()
    files = instance.get()
    for file in files:
        linhas = file["linhas_do_arquivo"]
        arquivo = file["nome_do_arquivo"]
        conta_linhas = 0
        for linha in linhas:
            linha = linha.replace(".", "")
            # print("------\n")
            # print(linha)
            palavras = linha.split(" ")
            conta_linhas += 1
            if word in palavras:
                ocorrencias.append({"linha": conta_linhas})
        result.append({
            "palavra": word,
            "arquivo": arquivo,
            "ocorrencias": ocorrencias
        })
        if len(ocorrencias) == 0:
            return []
    return result
    # TESTAR **********


def search_by_word(word, instance):
    pass


# project = Queue()
# process("statics/nome_pedro.txt", project)
# word = exists_word("Pedro", project)
# print(word)
