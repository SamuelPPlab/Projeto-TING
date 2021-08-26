import sys


def txt_importer(file_path):
    try:
        assert file_path.endswith(".txt")
        with open(file_path, "r") as file:
            contents = file.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {file_path} não encontrado\n")
    except AssertionError:
        sys.stderr.write("Formato inválido\n")
    else:
        return contents
