from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for i in range(instance.size()):
        if path_file == instance.search(i)["nome_do_arquivo"]:
            return None

    lines = txt_importer(path_file)
    if lines:
        instance.enqueue(
            {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(lines),
                "linhas_do_arquivo": lines,
            }
        )
        print(instance.search(instance.size() - 1))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
