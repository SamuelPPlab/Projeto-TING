import sys
import os
from ting_file_management.queue import Queue


def txt_importer(path_file):
    extension = path_file.split('.')[1]
    if extension != 'txt':
        return sys.stderr.write("Formato inválido\n")
    if not os.path.isfile(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    fila = Queue()
    with open(path_file, 'r') as file:
        for line in file:
            fila.enqueue(line.rstrip('\n'))

    return fila.display_queue()


# print(txt_importer('statics/arquivo_teste.txt'))
