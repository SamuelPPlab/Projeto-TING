from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if len(instance) < 1:
        file = txt_importer(path_file)
        resuslt = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }

    sys.stdout.write(str(resuslt))
    instance.enqueue(resuslt)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
