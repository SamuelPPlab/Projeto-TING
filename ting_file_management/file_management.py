import sys


def txt_importer(path_file):
    if not path_file.endswith("txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as f:
            contents = f.read().splitlines()
            return contents
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
