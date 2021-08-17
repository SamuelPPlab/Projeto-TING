import sys


def txt_importer(path_file):
    valid = path_file.endswith(".txt")
    try:
        if not valid:
            sys.stderr.write("Formato inválido\n")

        with open(path_file, 'r') as file:
            txt_file = file.read().splitlines()
            inventory = [row for row in txt_file]
            return inventory

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
