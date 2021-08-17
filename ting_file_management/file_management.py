import sys


# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            # https://www.w3schools.com/python/ref_string_splitlines.asp
            text_lines = file.read().splitlines()
            return text_lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
