import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file) as file:
            text = file.read().splitlines()
            return text
    except FileNotFoundError:
        # Template Literal
        return sys.stderr.write('Arquivo {path_file} não encontrado\n'.format(path_file=path_file))
