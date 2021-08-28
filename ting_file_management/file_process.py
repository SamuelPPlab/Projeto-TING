import sys
from .file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if (path_file == instance.search(index)['nome_do_arquivo']):
            return

    file = txt_importer(path_file)
    file_format = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file,
    }

    instance.enqueue(file_format)
    print(file_format)


def remove(instance):
    if (len(instance) == 0):
        print('Não há elementos')
        return

    file = instance.dequeue()
    filename = file['nome_do_arquivo']
    print(f'Arquivo {filename} removido com sucesso')


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
