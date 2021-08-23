import sys
# import os
from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue
# teste = Queue()


def process(path_file, instance):
    # nome_arquivo = os.path.basename(path_file)
    data = txt_importer(path_file)
    if len(instance) < 1:
        resp = {
            'nome_do_arquivo':  path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data
        }
        sys.stdout.write(str(resp))
        instance.enqueue(resp)


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    item_removed = instance.dequeue()
    file_removed = item_removed["nome_do_arquivo"]
    return sys.stdout.write(
        f"Arquivo {file_removed} removido com sucesso\n"
    )


def file_metadata(instance, position):
    if position > len(instance):
        return sys.stderr.write("Posição inválida\n")
    return instance.search(position)

# print(process("../statics/arquivo_teste.txt", teste))
