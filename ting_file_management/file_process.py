import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance._queue:
        instance.enqueue(path_file)

    print(
        f"'nome_do_arquivo': '{path_file}'\n",
        f"'qtd_linhas': {len(txt_importer(path_file))}'\n",
        f"'linhas_do_arquivo': {txt_importer(path_file)}'",
        file=sys.stdout,
        )


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    print(
        f"Arquivo {instance.dequeue()} removido com sucesso\n",
        file=sys.stdout,
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
