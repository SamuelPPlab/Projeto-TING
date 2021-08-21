import os.path
import sys


def txt_importer(path_file: str):
    """Aqui irá sua implementação"""
    if not os.path.isfile(path_file):
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return False
    with open(path_file, "r") as file:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")
            return False
        data = file.read().splitlines()
        return data


# txt_importer("statics/arquivo_teste.txt")
