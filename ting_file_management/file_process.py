import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if len(instance) < 1:
        imported = txt_importer(path_file)
        response = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(imported),
            "linhas_do_arquivo": imported
        }
        sys.stdout.write(str(response))
        instance.enqueue(response)


def remove(instance):
    if len(instance) <= 0:
        return sys.stdout.write("Não há elementos\n")
    list_item_removed = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {list_item_removed} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        return result
    except IndexError:
        sys.stderr.write("Posição inválida\n")
