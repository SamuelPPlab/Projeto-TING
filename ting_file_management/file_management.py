import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.split('.')[1] != 'txt':
        sys.stderr.write("Formato inválido\n")

    try:
        fd = open(path_file, 'r', encoding="utf8")  # fd = file data
        data = fd.read().splitlines()
        return data
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
