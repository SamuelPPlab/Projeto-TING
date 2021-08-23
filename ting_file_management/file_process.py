import sys
from ting_file_management.file_management import txt_importer


# 3.0 read file and add to row
def process(file_path, instance):

    if file_path.endswith('.txt'):
        file_li = txt_importer(file_path)
        file_finished = {}
        file_finished = {
            'nome_do_arquivo': file_path,
            'qtd_linhas': len(file_li),
            'linhas_do_arquivo': file_li
        }
    sys.stdout.write(str('{}\n'.format(file_finished)))
    instance.enqueue(file_finished)


# 4.0 remove file using dequeue
def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write('Não há elementos\n')

    file_rmve = instance.dequeue()['nome_do_arquivo']
    return sys.stdout.write(str(f'Arquivo {file_rmve} removido com sucesso\n'))


# 5.0 receive a position and check, then return data
def file_metadata(instance, position):
    # print('FP ')
    if position >= len(instance):
        return sys.stderr.write('Posição inválida\n')

    return sys.stdout.write(str(position))


# python3 -m pytest tests/test_file_process.py

# referencias
# same of file management file
