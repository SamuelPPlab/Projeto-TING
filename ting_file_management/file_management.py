import sys


def txt_importer(path_file):
    if path_file.split(".")[1] != "xml":
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            file.read().splitlines()  # @vanessaara
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")