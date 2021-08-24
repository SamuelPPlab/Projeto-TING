import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    instance_length = instance.__len__()
    if instance_length >= 1:
        return None
    else:
        content_file = txt_importer(path_file)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content_file),
            "linhas_do_arquivo": content_file
        }
        instance.enqueue(result)
        sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        path = instance.dequeue()["nome_do_arquivo"]
        instance.dequeue()
        if(instance.__len__() == 0):
            sys.stdout.write(f"Arquivo {path} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        result = instance.search(position)
        sys.stdout.write(str(result))
    except IndexError:
        sys.stderr.write("Posição inválida")
