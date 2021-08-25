import sys
import os

def txt_importer(path_file):
    if path_file.split('.')[1] != 'txt':
        return sys.stderr.write('Formato inválido\n')
    if not os.path.isfile(path_file):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    return open(path_file, 'r').read().splitlines()
