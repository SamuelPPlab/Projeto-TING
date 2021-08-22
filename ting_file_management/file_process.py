import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    txt_content = txt_importer(path_file)
    number_of_lines = len(txt_content)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas":  number_of_lines,
        "linhas_do_arquivo": txt_content
    }
    for sample in instance._queue:
        if sample["nome_do_arquivo"] == path_file:
            return
    instance.enqueue(data)
    sys.stdout.write(f"{data}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
