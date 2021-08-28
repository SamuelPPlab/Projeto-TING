import sys


def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, mode="r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(
            "Arquivo statics/arquivo_nao_existe.txt não encontrado",
            file=sys.stderr,
        )
