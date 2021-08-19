import sys


def txt_importer(path_file):
    """verificando se o final do arquivo é .txt"""
    if path_file[-4:] != ".txt":
        sys.stderr.write("Formato inválido\n")
    try:
        """retornando a estrutura com as linhas do arquivo"""
        with open(path_file) as file:
            return [line.replace("\n", "") for line in file]
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
