import sys
from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue


def process(path_file, instance):
    """Aqui irá sua implementação"""
    # file_name = path_file.split('/', 2)[1]
    if instance.__len__() < 1:
        txt_file = txt_importer(path_file)
        to_write = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_file),
            "linhas_do_arquivo": txt_file
        }

        sys.stdout.write(str(to_write))
        instance.enqueue(to_write)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
