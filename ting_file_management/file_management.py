import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    file_type = path_file.split(".")[1]
    if file_type != "txt":
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file) as textfile:
            lines = textfile.read()
        return lines.split("\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
