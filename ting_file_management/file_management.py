import sys
import os


# 2.2
def txt_importer(file_path):
    if not os.path.isfile(file_path):
        return sys.stderr.write(f'Arquivo {file_path} não encontrado\n')

    # 2.3 file_path.endswith('.txt')
    if file_path.split('.')[1] != 'txt':
        return sys.stderr.write('Formato inválido\n')

    # 2.1
    with open(file_path, 'r') as file:
        file_li = file.read().splitlines()
    return file_li


# python3 -m pytest tests/test_file_mangement.py

# referencias
# https://www.programiz.com/python-programming/methods/built-in/open
# https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
# https://www.programcreek.com/python/example/56344/sys.stderr.write
# https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
# https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
# https://www.geeksforgeeks.org/python-os-path-isfile-method/
