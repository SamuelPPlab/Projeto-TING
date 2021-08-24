import sys
from ting_file_management.file_management import txt_importer

# from queue import Queue


def process(path_file, instance):
    for index in range(len(instance)):
        if path_file in instance.search(index)["nome_do_arquivo"]:
            return None

    data = txt_importer(path_file)
    # instance.enqueue(data)

    info = dict(
        {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }
    )
    instance.enqueue(info)
    sys.stdout.write(f"{info}\n")


def remove(instance):
    if instance:
        filename = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {filename} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    if 0 < position < len(instance):
        sys.stdout.write(f"{instance.search(position)}")
    else:
        sys.stderr.write("Posição inválida")
