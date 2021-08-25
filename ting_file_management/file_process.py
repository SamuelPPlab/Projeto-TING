from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)

    for index in range(len(instance)):
        # verificando se há algum nome igual ao do path_file
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    data_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    instance.enqueue(data_info)
    sys.stdout.write(f'{data_info}\n')


def remove(instance):
    if len(instance) > 0:
        removed = instance.dequeue()['nome_do_arquivo']
        return sys.stdout.write(
            f'Arquivo {removed} removido com sucesso\n')
    return print('Não há elementos')


def file_metadata(instance, position):
    if position > len(instance):
        return sys.stderr.write('Posição inválida')
    return instance.search(position)
