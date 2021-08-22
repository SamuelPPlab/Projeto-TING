import sys


def txt_importer(path_file):
    if path_file[-3:] != "txt":
        message = "Formato inválido"
        print(message, file=sys.stderr)

    try:
        with open(path_file, "r") as txt_file:
            return [line.rstrip("\n") for line in txt_file.readlines()]

    except FileNotFoundError:
        message = "Arquivo statics/arquivo_nao_existe.txt não encontrado"
        print(message, file=sys.stderr)
