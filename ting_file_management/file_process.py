import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(instance.size()):
        if path_file == instance.search(index)["nome_do_arquivo"]:
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
    if instance.is_empty():
        print("Não há elementos")
    else:
        file_name = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {file_name} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
