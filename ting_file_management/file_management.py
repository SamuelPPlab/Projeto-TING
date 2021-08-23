import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)
    try:
        arr = []
        with open(path_file, "r") as file:
            for line in file.readlines():
                line = line.replace("\n", "")
                arr.append(line)
        return arr
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
