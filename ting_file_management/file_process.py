from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    arquivo = txt_importer(path_file)  # usando a função que fiz no req.2
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
    if len(instance) <= 0:
        return sys.stdout.write("Não há elementos\n")

    nome = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {nome} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        return instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")
