import sys


def txt_importer(path_file):
    if (path_file.split('.')[1] != 'txt'):
        return sys.stderr.write('Formato inválido\n')

    try:
        with open(path_file, 'r') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
