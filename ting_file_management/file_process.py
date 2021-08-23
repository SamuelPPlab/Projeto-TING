import os
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue

teste = Queue()

def process(path_file, instance):
    nome_arquivo = os.path.basename(path_file)
    tot_linhas = 0
    data = txt_importer(path_file)
    for index in range(len(data)):
        tot_linhas += index
    resp = {"nome_do_arquivo": nome_arquivo, "qtd_linhas": tot_linhas, "linhas_do_arquivo": data}
    instance.enqueue(resp)
    return resp
    
    
    # instance.enqueue()
    # return resp

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

print(process("../statics/arquivo_teste.txt", teste))