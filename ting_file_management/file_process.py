import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        if path_file == instance.search([i][0])["nome_do_arquivo"]:
            return None

    _file = txt_importer(path_file)
    process_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(_file),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    instance.enqueue(process_file)

    print(instance.search(len(instance) - 1))


def remove(instance):
    """Aqui irá sua implementação"""
    if not len(instance):
        print("Não há elementos")
    else:
        removed = instance.dequeue()
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        searched_file = instance.search(position)
        return print(searched_file)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
