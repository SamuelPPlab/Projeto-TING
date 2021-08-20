import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if (
            path_file == instance.search(index)["nome_do_arquivo"]
        ):  # if @MoisesSantana
            return None

    file_text = txt_importer(path_file)
    length = len(file_text)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": length,
        "linhas_do_arquivo": file_text,
    }
    instance.enqueue(data)
    sys.stdout.write(f"{data}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
