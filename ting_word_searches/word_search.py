# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    document = list()
    new_object = {
        "palavra": word,
        "arquivo": "",
        "ocorrencias": []
    }

    for i in range(len(instance)):
        file = instance.search(i)

        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                new_object["palavra"] = word
                new_object["arquivo"] = file["nome_do_arquivo"]
                new_object["ocorrencias"] = [{"linha": i + 1}]
    if len(new_object["ocorrencias"]) == 0:
        return []
    document.append(new_object)
    return document


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# if __name__ == "__main__":
#     project = Queue()
#     process("statics/nome_pedro.txt", project)
#     print()
#     word = exists_word("Pedro", project)
#     print(word)
