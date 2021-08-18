import sys


def txt_importer(path_file):
    extension = path_file[-4:]
    if extension != ".txt":
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            text_lines = list()
            text_lines = file.read().split("\n")
            return text_lines
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
