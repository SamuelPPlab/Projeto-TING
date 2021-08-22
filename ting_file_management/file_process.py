import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if len(instance) > 0:
        pass
    else:
        array = txt_importer(path_file)
        file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(array),
            "linhas_do_arquivo": array
        }
        sys.stdout.write(f"{file}\n")
        instance.enqueue(file)


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write('Não há elementos\n')
        pass
    else:
        removed = instance.dequeue()
        if bool(removed):
            path = removed['nome_do_arquivo']
            sys.stdout.write(f'Arquivo {path} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(file)
    except IndexError:
        sys.stderr.write('Posição inválida\n')
