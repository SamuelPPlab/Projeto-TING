import sys


def txt_importer(path_file):
    try:
        with open(path_file, "r", encoding="utf-8") as file:
            content_file = []
            if path_file.split('.')[-1] == 'txt':
                for readline in file:
                    content_file.append(readline.rstrip('\n'))
                return content_file
            sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
