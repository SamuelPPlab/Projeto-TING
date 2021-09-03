import sys
import os


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    if not os.path.isfile(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    with open(path_file, "r") as file:
        return file.read().splitlines()
