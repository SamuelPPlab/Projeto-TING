from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    file = []
    for item in range(instance.__len__()):
        data = instance.search(item)["linhas_do_arquivo"]
        teste = find_word(word, data, False)
        if teste == []:
            return file
        else:
            file.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(item)["nome_do_arquivo"],
                    "ocorrencias": teste,
                }
            )
    return file


def find_word(word, data, complete):
    """Aqui irá sua implementação"""
    # result = []
    index = 0
    lista = []
    for linha in data:
        index += 1
        resultado = linha.lower().find(word.lower())
        if resultado >= 0:
            if complete:
                lista.append({"linha": index, "conteudo": linha})
            else:
                lista.append({"linha": index})

        # result.append(
        # {
        #     "palavra": word,
        #     "arquivo": instance.search(item)["linhas_do_arquivo"],
        #     "ocorrencias": lista,
        # }
        # )
    return lista


def search_by_word(word, instance):
    file = []
    for item in range(instance.__len__()):
        data = instance.search(item)["linhas_do_arquivo"]
        teste = find_word(word, data, True)
        if teste == []:
            return file
        else:
            file.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(item)["nome_do_arquivo"],
                    "ocorrencias": teste,
                }
            )
    return file


if __name__ == "__main__":
    project = Queue()
    # print(project)
    process("statics/nome_pedro.txt", project)
    print(exists_word("Ratinho", project))

# Pair programming: Moacyr, Renato e Emerson | Agradecimentos especiais Tulio.
