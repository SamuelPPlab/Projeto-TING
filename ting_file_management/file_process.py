from .file_management import txt_importer
import sys


def process(path_file, instance):
    flag = False
    file = txt_importer(path_file)
    for i in instance._data:
        if i.get("nome_do_arquivo") == path_file:
            flag = True
    if flag is False:
        content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        instance.enqueue(content)
        print(content, file=sys.stdout)


def remove(instance):
    if len(instance._data) < 1:
        print("Não há elementos")
    else:
        value = instance.dequeue().get("nome_do_arquivo")
        print(
            f"Arquivo {value} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    try:
        value = instance.search(position)
        print(value, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
