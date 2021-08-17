import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError()
        with open(path_file, "r") as file:
            content = file.read()
        return content.splitlines()
    except OSError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError:
        print("Formato inválido", file=sys.stderr)
