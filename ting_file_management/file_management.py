import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        # tip from @carolbezerra-dev
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, 'r',) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(
            "Arquivo statics/arquivo_nao_existe.txt não encontrado\n"
            )
