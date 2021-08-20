from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    result = list()
    new_obj = {
        "palavra": word,
        "arquivo": None,
        "ocorrencias": list(),
    }
    for index in range(len(instance)):
        for i, v in enumerate(instance.search(index)["linhas_do_arquivo"]):
            if word.lower() in v.lower():
                new_obj["arquivo"] = instance.search(index)["nome_do_arquivo"]
                new_obj["ocorrencias"].append({"linha": i + 1})
                result.append(new_obj)
    return result


def search_by_word(word, instance):
    result = list()
    new_obj = {
        "palavra": word,
        "arquivo": None,
        "ocorrencias": list(),
    }
    for index in range(len(instance)):
        for i, v in enumerate(instance.search(index)["linhas_do_arquivo"]):
            if word.lower() in v.lower():
                new_obj["arquivo"] = instance.search(index)["nome_do_arquivo"]
                new_obj["ocorrencias"].append({"linha": i + 1, "conteudo": v})
                result.append(new_obj)
    return result


if __name__ == "__main__":
    # TESTE 1
    # assert word == text_exists_word
    # project = Queue()
    # process("statics/nome_pedro.txt", project)
    # word = exists_word("Pedro", project)
    # print(word)

    # TESTE 2
    # assert word == text_search_by_word
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = search_by_word("pedro", project)
    print(word)
