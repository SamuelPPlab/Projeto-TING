from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if len(instance) < 1:
        file = txt_importer(path_file)

        file_processed = dict()
        teste = len(file)
        file_processed['nome_do_arquivo'] = path_file
        file_processed['qtd_linhas'] = len(file)
        file_processed['linhas_do_arquivo'] = file

        instance.enqueue(file_processed)
        sys.stdout.write("{file_processed}".format(file_processed=file_processed))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
