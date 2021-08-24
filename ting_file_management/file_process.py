import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if path_file == instance.search(i).get("nome_do_arquivo"):
            return

    lines = txt_importer(path_file)

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(file_info)
    print(file_info)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")

    removed = instance.dequeue()
    removed_filename = removed.get("nome_do_arquivo")

    print(f"Arquivo {removed_filename} removido com sucesso")


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
