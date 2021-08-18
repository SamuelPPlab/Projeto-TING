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
    if len(instance):
        result = instance.dequeue()
        if result:
            name_file = result["nome_do_arquivo"]
            return sys.stdout.write(
                f'Arquivo {name_file} removido com sucesso\n')
    return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        return sys.stderr.write('Posição inválida\n')

    search = instance.search(position)
    result = f"'nome_do_arquivo': '{search['nome_do_arquivo']}'\n"
    result += f"'qtd_linhas': {search['qtd_linhas']}\n 'linhas_do_arquivo': {search['qtd_linhas']}"

    return sys.stdout.write(result)


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
#     # print('\n', len(queue))
#     print('\n\n\n', file_metadata(queue, 10))
#     # print('\n', len(queue))
