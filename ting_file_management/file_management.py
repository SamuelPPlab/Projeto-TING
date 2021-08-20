import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            raise TypeError()
        with open(path_file, mode='r') as file:
            lines = file.read().split('\n')
            return lines

    except TypeError:
        print('Formato inválido', file=sys.stderr)
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
