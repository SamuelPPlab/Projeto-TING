import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if '.txt' in path_file:
            with open(path_file) as txt_File:
                if txt_File:
                    news = txt_File.read().splitlines()
                    return list(news)
                sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
