import sys


def txt_importer(path_file):
    extension = path_file.split('.', -1)[-1]
    if extension != 'txt':
        sys.stderr.write("Formato inválido\n")
        return False
    try:
        lines = ''
        with open(path_file, 'r', newline='\n') as file:
            lines = file.read()
        file.close()
        return lines.split('\n')
    except(FileNotFoundError):
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
