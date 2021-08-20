import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    qtd_lines = len(file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": qtd_lines,
        "linhas_do_arquivo": file,
    }

    sys.stdout.write(f"{result}")


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    file_to_remove = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    return sys.stdout.write(f"Arquivo {file_to_remove} removido com sucesso\n")


def file_metadata(instance, position):
    if position < 0:
        file_name = instance.search(position)
        sys.stdout.write(f"{file_name}")
    else:
        sys.stderr.write("Posição inválida")
