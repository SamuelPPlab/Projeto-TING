import sys
# import os
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
# teste = Queue()

def process(path_file, instance):
    # nome_arquivo = os.path.basename(path_file)
    tot_linhas = 0
    data = txt_importer(path_file)
    # for index in range(len(data)):
    #     tot_linhas += index
    resp = {'nome_do_arquivo':  path_file, "qtd_linhas": len(data), "linhas_do_arquivo": data}
    sys.stdout.write(str(resp))
    instance.enqueue(resp)
    # instance.enqueue()
    # return resp

def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

# print(process("../statics/arquivo_teste.txt", teste))