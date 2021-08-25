from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    shape = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    instance.enqueue(shape)

    print(shape)


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        file = instance.dequeue()
        print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos")
        # @brunasg


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        element = instance.search(position)
        print(element)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
