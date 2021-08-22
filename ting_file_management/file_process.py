# from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) > 1:
        sys.stdout.write(f"Arquivo {instance} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        sys.stdout.write(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida")
