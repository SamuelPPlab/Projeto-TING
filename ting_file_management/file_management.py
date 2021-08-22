import sys


def txt_importer(path_file):
    if not (path_file.endswith('.txt')):
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as f:
            lines = f.readlines()
            lines = [line.rstrip() for line in lines]
            return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
