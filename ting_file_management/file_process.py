import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text = txt_importer(path_file)
    number_of_lines = len(text)
    format = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": number_of_lines,
        "linhas_do_arquivo": text
    }
    sys.stdout.write(str(format))
    instance.enqueue(format)


def remove(instance):
    if len(instance) < 1:
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        search_by_position = instance.search(position)
        return sys.stdout.write(str(search_by_position))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
