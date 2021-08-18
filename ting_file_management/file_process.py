import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text = txt_importer(path_file)
    lines_number = len(text)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lines_number,
        "linhas_do_arquivo": text,
    }
    sys.stdout.write(f"{result}")
    instance.enqueue(result)


def remove(instance):
    current_queue = instance._data
    if len(current_queue) == 0:
        return sys.stdout.write("Não há elementos\n")
    first_item = instance.dequeue()
    file_name = first_item["nome_do_arquivo"]

    return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    if position > len(instance):
        return sys.stderr.write("Posição inválida\n")
