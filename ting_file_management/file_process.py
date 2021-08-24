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
    sys.stdout.write(f"{dic}")


def remove(instance):
    if len(instance) > 0:
        nome = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {nome} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    if position < len(instance):
        sys.stdout.write(f"{instance.search(position)}\n")
    else:
        sys.stderr.write("Posição inválida\n")


if __name__ == "__main__":
    project = Queue()
    print(process("statics/arquivo_teste.txt", project))
