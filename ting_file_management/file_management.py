import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            sys.stderr.write("Formato inválido\n")
        with open(path_file) as txt_file:
            content = txt_file.read().split("\n")
            text = list(row for row in content)
            return text
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
