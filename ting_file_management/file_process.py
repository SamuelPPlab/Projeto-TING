# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)
    processed_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": data.__len__(),
        "linhas_do_arquivo": data,
    }
    if processed_content not in instance.display_queue():
        instance.enqueue(processed_content)
    return sys.stdout.write(f"{processed_content}")


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    deleted_item = instance.dequeue()
    path_name = deleted_item["nome_do_arquivo"]
    return print(
        f'Arquivo {path_name} removido com sucesso'
    )


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        sys.stderr.write('Posição inválida')


# print(process('statics/arquivo_teste.txt', Queue()))
# print(process('statics/arquivo_teste.txt', Queue()))
# my_list = Queue()
# processed_content = {
#         "nome_do_arquivo": "arquivo.txt",
#         "qtd_linhas": 3,
#         "linhas_do_arquivo": ["abc", "efg"],
#     }
# my_list.enqueue(processed_content)
# print(file_metadata(my_list, 1))
