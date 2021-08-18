import sys
from ting_file_management.file_management import txt_importer

# from ting_file_management.queue import Queue
# from queue import Queue


def process(path_file, instance):
    nome_do_arquivo = path_file
    qtd_linhas = len(txt_importer(path_file))
    linhas_do_arquivo = txt_importer(path_file)
    process_content = {
        "nome_do_arquivo": nome_do_arquivo,
        "qtd_linhas": qtd_linhas,
        "linhas_do_arquivo": linhas_do_arquivo,
    }
    #   REVER TODA ESSA PARTE - DEVE-SE IGNORAR ARQUIVO COM NOME REPETIDO
    last_file = instance.search(len(instance) - 1)
    print(last_file)
    if last_file.nome_do_arquivo != nome_do_arquivo:
        # -------------------------
        instance.enqueue(process_content)
    return sys.stdout.write(str(process_content))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# new_queue = Queue()
# print(process("statics/arquivo_teste.txt", new_queue))
