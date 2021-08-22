from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    arquivo = txt_importer(path_file)  # usando afunção que fiz no req.2
    conta_linhas = len(arquivo)  # cada linha é 1 item
    dict_retorno = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": conta_linhas,
        "linhas_do_arquivo": arquivo
        }  # saída esperada

    instance.enqueue(dict_retorno)  # adiciona na lista
    sys.stdout.write(f"{dict_retorno}")
    # a saída tem que ter esse out, referência: Luíse Rios


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

