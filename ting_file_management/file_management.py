import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")

        with open(path_file, "r") as file:
            content = file.read().split("\n")
            return [line for line in content]

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
