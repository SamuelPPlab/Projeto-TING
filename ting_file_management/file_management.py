# Referencia splitlines: https://www.w3schools.com/python/ref_string_splitlines.asp


import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            readed_file = file.read()
            return readed_file.splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
