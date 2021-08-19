from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance):
    my_data = dict()
    data_len = len(txt_importer(path_file))
    my_data["nome_do_arquivo"] = path_file
    my_data["qtd_linhas"] = data_len
    my_data["linhas_do_arquivo"] = txt_importer(path_file)
    get_data = instance._data
    if my_data not in get_data:
        instance.enqueue(my_data)
    # https://www.geeksforgeeks.org/sys-stdout-write-in-python/
    return sys.stdout.write(f"{my_data}")


def remove(instance):
    get_data = instance._data
    length = instance.__len__()
    if length == 0:
        return sys.stdout.write("Não há elementos\n")
    print(get_data)
    remove_item = instance.dequeue()
    print(get_data)
    path_file = remove_item["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        find_data = instance.search(position)
        return sys.stdout.write(f"{find_data}")
    except IndexError:
        return sys.stderr.write("Posição inválida")




project2 = Queue()
teste1 = process("statics/arquivo_teste.txt", project2)
teste = file_metadata(project2, 0)
print(teste1)
print("ola", teste)
