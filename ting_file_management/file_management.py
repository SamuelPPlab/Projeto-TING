import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')
    try:
        file = open(path_file, 'r')
        file_list = list()
        for row in file:
            file_list.append(row.rstrip('\n'))
        return file_list
    except IOError:
        error_message = f'Arquivo {path_file} não encontrado\n'
        sys.stderr.write(error_message)
