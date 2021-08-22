import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.is_used_file(path_file):
        return

    content = txt_importer(path_file)
    processed_file = {}

    processed_file['nome_do_arquivo'] = path_file
    processed_file['qtd_linhas'] = len(content)
    processed_file['linhas_do_arquivo'] = content

    instance.enqueue(processed_file)
    sys.stdout.write(str(processed_file))


def remove(instance):
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')

    removed_file = instance.dequeue()['nome_do_arquivo']

    sys.stdout.write(f'Arquivo {removed_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        info = instance.search(position)

        return sys.stdout.write(str(info))

    except IndexError:
        return sys.stderr.write('Posição inválida')
