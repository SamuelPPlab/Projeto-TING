import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        return open(path_file, "r").read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
