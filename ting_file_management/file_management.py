import sys
import os.path


def readTxt(path_file):
    with open(path_file, 'r',) as file:
        return file.read().splitlines()


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            raise ValueError()
        if not (os.path.exists(path_file)):
            raise FileNotFoundError()
        return readTxt(path_file)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError:
        print(f"Formato inválido", file=sys.stderr)
