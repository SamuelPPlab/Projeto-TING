import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError()
        with open(path_file, "r", newline="\n") as txt_file:
            text = txt_file.read()
            print(text)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
    except ValueError:
        print("Formato inválido", file=sys.stderr)
        return None
    return text.split("\n")
