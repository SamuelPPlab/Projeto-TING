from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue

# import os
# import sys


def process(path_file: str, instance: Queue):
    file_content = txt_importer(path_file)

    for archive in instance.get_data():
        if archive["nome_do_arquivo"] == path_file:
            return False
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    if file_content:
        instance.enqueue(file)
        print(file)


def remove(instance: Queue):
    if len(instance.get_data()) == 0:
        print("Não há elementos")
    else:
        value = instance.dequeue()
        print(f"Arquivo {value['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


fila_data = Queue()
# fila_data.enqueue()
process("statics/arquivo_teste.txt", fila_data)
