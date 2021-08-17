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
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        file_name = instance.search(0)["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")
        instance.dequeue()


def file_metadata(instance, position):
    try:
        file_name = instance.search(position)
        sys.stdout.write(f"{file_name}")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
