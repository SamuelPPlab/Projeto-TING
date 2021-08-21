import sys
import os


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')
    if not os.path.isfile(path_file):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

    file = open(path_file, 'r').read().splitlines()
    return file
