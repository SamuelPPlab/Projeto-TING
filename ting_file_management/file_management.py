import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file[-4:] != '.txt':
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file) as fd:
            return fd.read().split('\n')
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
