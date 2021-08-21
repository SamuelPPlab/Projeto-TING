import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file_name = path_file
    file_content = txt_importer(path_file)
    file = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content
    }
    try:
        instance.enqueue(file)
        sys.stdout.write(str(file))
    except NameError:
        pass


def remove(instance):
    """Aqui irá sua implementação"""
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")
    file = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida")
