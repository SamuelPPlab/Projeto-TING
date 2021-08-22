import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    txt_content = txt_importer(path_file)
    number_of_lines = len(txt_content)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas":  number_of_lines,
        "linhas_do_arquivo": txt_content
    }
    for sample in instance._queue:
        if sample["nome_do_arquivo"] == path_file:
            return
    instance.enqueue(data)
    sys.stdout.write(f"{data}")


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    removed = instance.dequeue()
    file_name = removed["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    if position >= len(instance):
        return sys.stderr.write("Posição inválida")
    return instance.search(position)
