from .file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    target = False
    file = txt_importer(path_file)
    print(file)
    for index in instance._data:
        if index.get("nome_do_arquivo") == path_file:
            target = True
    if target is False:
        content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        instance.enqueue(content)
        print(content, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance._data) < 1:
        print("Não há elementos")
    else:
        remove = instance.dequeue().get("nome_do_arquivo")
        print(
            f"Arquivo {remove} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        size = instance.search(position)
        print(size, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
