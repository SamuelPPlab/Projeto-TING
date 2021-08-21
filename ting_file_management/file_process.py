import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        if file_metadata(instance, i)["nome_do_arquivo"] == path_file:
            return
    contents = txt_importer(path_file)
    value = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(contents),
        "linhas_do_arquivo": contents
    }
    print(value)
    instance.enqueue(value)


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        value = instance.dequeue()
        print(f"Arquivo {value['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        return instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
