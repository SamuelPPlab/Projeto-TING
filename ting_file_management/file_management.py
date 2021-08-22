import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, 'r') as text:
            return [line.replace("\n", "") for line in text]

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
