import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if len(instance) < 1:
        imported = txt_importer(path_file)
        response = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(imported),
            "linhas_do_arquivo": imported
        }
        sys.stdout.write(str(response))
        instance.enqueue(response)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
