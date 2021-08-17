import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    if path_file not in instance.data_names():
        instance.enqueue(path_file)
    return print(
        f"'nome_do_arquivo': '{path_file}'\n",
        f"'qtd_linhas': {len(file)}'\n",
        f"'linhas_do_arquivo': {file}'",
    )


def remove(instance):
    if instance.__len__() == 0:
        return print("Não há elementos")
    file_removed = instance.dequeue()
    return print(f"Arquivo {file_removed} removido com sucesso\n")


def file_metadata(instance, position):
    if position < 0 or position >= instance.__len__():
        return sys.stderr.write("Posição inválida")
    return print(txt_importer(instance.search(position)))
