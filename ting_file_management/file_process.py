from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    content_file = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content_file),
        "linhas_do_arquivo": content_file
    }
    sys.stdout.write(str(new_dict))
    instance.enqueue(new_dict)

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
