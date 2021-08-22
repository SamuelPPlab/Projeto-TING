import sys
import os


def txt_importer(path_file):
    if path_file.endswith('.txt'):
        if not os.path.isfile(path_file):
            return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        with open(path_file, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    else:
        return sys.stderr.write('Formato inválido\n')
