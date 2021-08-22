import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if len(instance) > 0:
        pass
    else:
        array = txt_importer(path_file)
        file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(array),
            "linhas_do_arquivo": array
        }
        sys.stdout.write(f"{file}\n")
        instance.enqueue(file)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
