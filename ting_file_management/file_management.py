import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, mode="r") as file:
            file_read = file.read().split("\n")
            return file_read
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
