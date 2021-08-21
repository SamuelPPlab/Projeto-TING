import sys

def txt_importer(path_file):
    if path_file[-4:] != '.txt':
        sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file) as news_file:
            return news_file.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")