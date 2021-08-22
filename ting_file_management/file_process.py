from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file: str, instance: Queue):

    line = txt_importer(path_file)

    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(line),
        "linhas_do_arquivo": line,
    }

    instance.enqueue(file)

    print(file, file=sys.stdout)


def remove(instance):
    try:
        instance.dequeue()
        message = "Arquivo statics/arquivo_teste.txt removido com sucesso"
        print(message, file=sys.stdout)
    except IndexError:
        message = "Não há elementos"
        print(message, file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        message = "Posição inválida"
        print(message, file=sys.stderr)
