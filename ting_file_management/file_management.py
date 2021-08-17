import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith("txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            content = file.read().splitlines()
            return content
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
