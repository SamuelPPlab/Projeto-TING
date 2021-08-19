import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    textArray = txt_importer(path_file)
    resultObj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(textArray),
        "linhas_do_arquivo": textArray,
    }
    sys.stdout.write(f"{resultObj}")


def remove(instance):
    if (len(instance) > 0):
        removedItem = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {removedItem} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        sys.stdout.write(f"{file_data}")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
