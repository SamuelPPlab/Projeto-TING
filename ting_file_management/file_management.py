import sys


def get_file_text(path_file):
    try:
        with open(path_file) as fd:
            lines = fd.readlines()
            return lines
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


def txt_importer(path_file):
    if not (path_file.endswith('.txt')):
        return sys.stderr.write("Formato inválido\n")

    get_file_text(path_file)
