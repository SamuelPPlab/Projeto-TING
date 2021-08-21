from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    process_file = {}
    file = txt_importer(path_file)
    process_file['nome_do_arquivo'] = path_file
    process_file['qtd_linhas'] = len(file)
    process_file['linhas_do_arquivo'] = file
    instance.enqueue(process_file)
    sys.stdout.write(f"{process_file}\n")
    return process_file


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
