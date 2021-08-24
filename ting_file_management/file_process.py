import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for x in range(len(instance)):
        if path_file in instance.search(x)["nome_do_arquivo"]:
            return None

    arquivo = txt_importer(path_file)
    dic = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(arquivo),
        "linhas_do_arquivo": arquivo,
    }
    instance.enqueue(dic)
    sys.stdout.write(f"{dic}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    project = Queue()
    print(process("statics/arquivo_teste.txt", project))
