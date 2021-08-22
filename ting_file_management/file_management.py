import sys
import os.path

def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            raise ValueError()
        with open(path_file, 'r',) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError:
        print(f"Formato inválido", file=sys.stderr)
