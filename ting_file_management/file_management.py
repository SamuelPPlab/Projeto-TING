import sys


def txt_importer(path_file):
    extension_file = path_file.split(".").pop()
    if extension_file != "txt":
        sys.stderr.write("Formato inválido\n")
    try:
        file = open(path_file)
        return file.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
