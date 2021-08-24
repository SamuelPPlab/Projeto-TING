from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_read = txt_importer(path_file)
    file_processing = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": file_read.__len__(),
        "linhas_do_arquivo": file_read,
    }

    for file in range(instance.__len__()):
        if instance.search(file)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(file_processing)
    sys.stdout.write(f"{file_processing}")


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    file_remove = instance.dequeue()
    file_removed_name = file_remove["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_removed_name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file_search = instance.search(position)
        sys.stdout.write(f"{file_search}")
    except IndexError:
        sys.stderr.write("Posição inválida")
