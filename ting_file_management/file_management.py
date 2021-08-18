import sys


def txt_importer(path_file):
    try:
        if '.txt' not in path_file:
            sys.stderr.write('Formato inválido\n')
            return
        content = open(path_file, "r")
        result = content.read().splitlines()

    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    else:
        content.close()
        return result


# if __name__ == "__main__":
#     arquivo = txt_importer("statics/arquivo_teste33.txt")
#     print(arquivo)
