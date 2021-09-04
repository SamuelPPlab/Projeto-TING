import sys


def txt_importer(path):
    if '.txt' not in path:
        return sys.stderr.write('Formato inválido\n')

    try:
        with open(path) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            return lines
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path} não encontrado\n')
