import sys


def txt_importer(path_file):
    try:
        if path_file.endswith("txt"):
            with open(path_file, mode="r") as file:
                content = file.read()
                return content.split("\n")
        else:
            sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
