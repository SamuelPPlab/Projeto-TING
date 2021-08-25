import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    text = txt_importer(path_file)
    lines = len(text)
    shape = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lines,
        "linhas_do_arquivo": text
    }
    sys.stdout.write(str(shape))
    instance.enqueue(shape)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
