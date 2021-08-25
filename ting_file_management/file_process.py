import sys

from .file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    instance.enqueue(processed_data)
    sys.stdout.write(str(processed_data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
