import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

# O splitlines()método divide uma string em uma lista.
# A divisão é feita nas quebras de linha.
# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
# try,except https://www.youtube.com/watch?v=RHSxIKGCX7c
