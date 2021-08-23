from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines = txt_importer(path_file)
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    instance.enqueue(file)
    print(file, file=sys.stdout)


def remove(instance):
    try:
        file = instance.dequeue()
        name = file['nome_do_arquivo']
        message = 'Arquivo ' + name + ' removido com sucesso'
        print(message, file=sys.stdout)
    except IndexError:
        print('Não há elementos', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
