import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    lines = []
    filenotexist_text = f"Arquivo {path_file} não encontrado\n"
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "rt", newline="\n") as file:

                lines = [line.strip() for line in file]
                return lines

        else:
            sys.stderr.write("Formato inválido\n")

    except FileNotFoundError:
        sys.stderr.write(filenotexist_text)
