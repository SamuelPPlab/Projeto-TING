import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""

    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return

    content = txt_importer(path_file)

    obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }

    print(obj)
    instance.enqueue(obj)


def remove(instance: Queue):
    """Aqui irá sua implementação"""

    try:
        value = instance.dequeue()
        print(f"Arquivo {value['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
