import sys
from ting_file_management.file_management import txt_importer


def process(path, instance):
    for el in range(len(instance)):
        if instance.search(el)['nome_do_arquivo'] == path:
            return False

    lines = txt_importer(path)
    length = len(lines)
    processedFile = {
        'nome_do_arquivo': path,
        'qtd_linhas': length,
        'linhas_do_arquivo': lines
    }

    instance.enqueue(processedFile)

    return sys.stdout.write(f'{processedFile}')


def remove(instance):
    try:
        instance.search(0)
        path = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f'Arquivo {path} removido com sucesso\n')
    except Exception:
        sys.stdout.write('Não há elementos\n')


def file_metadata(instance, position):
    try:
        q_return = instance.search(position)
        sys.stdout.write(f'{q_return}')
    except Exception:
        sys.stderr.write('Posição inválida')
