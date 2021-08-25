from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    file_processed = dict()
    file_processed["nome_do_arquivo"] = path_file
    file_processed["qtd_linhas"] = len(file)
    file_processed["nome_do_arquivo"] = file


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
