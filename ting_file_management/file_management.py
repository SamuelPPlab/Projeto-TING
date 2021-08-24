import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            line = file.read().splitlines()

    except IOError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        return line
