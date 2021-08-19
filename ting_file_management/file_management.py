import sys

# https://www.w3schools.com/python/ref_string_splitlines.asp
# http://devfuria.com.br/python/manipulando-arquivos-de-texto/
# Tentei fazer com um if, mas o teste não passa, ai fui com try/except e foi


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")
        with open(path_file, "r", encoding="utf8") as data:
            return data.read().splitlines()
    # Acho que o teste espera esse except, já que aparece no log
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
