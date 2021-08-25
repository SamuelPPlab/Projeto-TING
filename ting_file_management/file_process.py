import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file_text = txt_importer(path_file)
    content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_text),
        "linhas_do_arquivo": file_text, }
    sys.stdout.write(f"{content}")
    instance.enqueue(content)


def remove(instance):
    if len(instance) > 0:
        file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        sys.stdout.write(f"{result}")
    except IndexError:
        return sys.stderr.write("Posição inválida")
