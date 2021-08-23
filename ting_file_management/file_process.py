import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    file_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    instance.enqueue(file_process)

    print(file_process)

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
