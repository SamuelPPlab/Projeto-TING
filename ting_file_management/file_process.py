import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for posicao in range(instance.size()):
        if path_file == instance.search(posicao)["nome_do_arquivo"]:
            return None
    arquivo = txt_importer(path_file)
    retorno = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(arquivo),
        "linhas_do_arquivo": arquivo
    }
    sys.stdout.write(f"{retorno}\n")
    return instance.enqueue(retorno)


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    removido = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {removido} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")
