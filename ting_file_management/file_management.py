import sys
import os.path


def readTxt(path_file):
    with open(path_file, 'r',) as file:
        return file.read().splitlines()


def txt_importer(path_file):
    try:
        if path_file.endswith('.txt'):
            if os.path.exists(path_file):
                return readTxt(path_file)
            else:
                raise FileNotFoundError()
        else:
            raise ValueError()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError:
        print(f"Formato inválido", file=sys.stderr)
