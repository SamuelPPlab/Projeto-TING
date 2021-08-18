import sys

from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    if instance.__len__() < 1:
        file = txt_importer(path_file)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        sys.stdout.write(str(result))
        instance.enqueue(result)


def remove(instance):
    """Aqui irá sua implementação"""
    length = instance.__len__()
    if length <= 0:
        return sys.stdout.write("Não há elementos\n")
    deq = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {deq} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        search = instance.search(position)
        return sys.stdout.write(str(search))
    except IndexError:
        sys.stderr.write("Posição inválida")


if __name__ == "__main__":
    project = Queue()
    # print(project)
    process("statics/arquivo_teste.txt", project)
