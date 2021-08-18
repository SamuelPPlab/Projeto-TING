import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    file = txt_importer(path_file)
    data = instance.__iter__()
    file_names = {item["nome_do_arquivo"] for item in data}
    if path_file not in file_names:
        content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
        result = f"'nome_do_arquivo': '{path_file}'\n"
        result += f"'qtd_linhas': {len(file)}\n 'linhas_do_arquivo': {file}"
        instance.enqueue(content)
        return sys.stdout.write(result)


def remove(instance):
    result = instance.dequeue()
    if result:
        sys.stdout(f'Arquivo removido com sucesso')

    # if len(instance) == 0:
    #     return sys.stdout('Não há elementos')

    # if result:
    #     sys.stdout(f'Arquivo {path_file} removido com sucesso')
    #     return


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# if __name__ == "__main__":
#     queue = Queue()
#     data = queue.__iter__()
#     path = "statics/arquivo_teste.txt"
#     result = process(path, queue)
#     result = process(path, queue)
#     result = process(path, queue)
#     result = process(path, queue)
#     # print(len(queue))
#     # print(result)
#     path = "statics/nome_pedro.txt"
#     result = process(path, queue)
#     result = process(path, queue)
#     result = process(path, queue)
#     data = queue.__iter__()

#     # print('\n\n', "statics/arquivo_teste.txt" in data[0]["nome_do_arquivo"])
