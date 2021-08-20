import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, mode="r") as file:
            linhasLidas = file.read().split("\n")
            return linhasLidas
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
