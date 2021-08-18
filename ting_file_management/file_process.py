import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    file = txt_importer(path_file)
    qtd_lines = len(file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": qtd_lines,
        "linhas_do_arquivo": file,
    }

    sys.stdout.write(f"{result}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
