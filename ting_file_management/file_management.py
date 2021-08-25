import sys
import os


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido')

    if not os.path.isfile(path_file):
        # https://www.geeksforgeeks.org/python-os-path-isfile-method/
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

    with open(path_file) as file:
        # https://www.w3schools.com/python/ref_string_splitlines.asp
        return file.read().splitlines()
