import sys


def txt_importer(path_file):
    try:
        if path_file[-4:] != ".txt":
            raise ValueError()
        with open(path_file, "r") as f:
            txt = f.read()
            return txt.split("\n")
        print(array)
        return array
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError:
        print("Formato inválido", file=sys.stderr)


if __name__ == "__main__":
    txt_importer("statics/arquivo_teste.txt")
