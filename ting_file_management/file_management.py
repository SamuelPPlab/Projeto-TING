import sys


def txt_importer(path_file):

    # source of file extension check:
    # https://github.com/tryber/sd-07-project-ting/
    # blob/rodolfo-project-ting/ting_file_management/
    # file_management.py
    if (path_file[-3:] != 'txt'):
        print('Formato inválido', file=sys.stderr)

    try:
        file = open(path_file, 'r')
        return file.read().split('\n')
    except FileNotFoundError:
        print(
            'Arquivo statics/arquivo_nao_existe.txt não encontrado',
            file=sys.stderr
        )
