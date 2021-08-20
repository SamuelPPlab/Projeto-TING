import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    nome_do_arquivo = path_file
    qtd_linhas = len(txt_importer(path_file))
    linhas_do_arquivo = txt_importer(path_file)
    conteudo_do_processo = {
        "nome_do_arquivo": nome_do_arquivo,
        "qtd_linhas": qtd_linhas,
        "linhas_do_arquivo": linhas_do_arquivo,
    }
    if len(instance) > 0:
        ultimo_arquivo = instance.search(len(instance) - 1)
        if ultimo_arquivo["nome_do_arquivo"] != nome_do_arquivo:
            instance.enqueue(conteudo_do_processo)
    else:
        instance.enqueue(conteudo_do_processo)
    return sys.stdout.write(str(conteudo_do_processo))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    file_to_remove = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    return sys.stdout.write(f"Arquivo {file_to_remove} removido com sucesso\n")


def file_metadata(instance, position):
    if position < 0:
        file_name = instance.search(position)
        sys.stdout.write(f"{file_name}")
    else:
        sys.stderr.write("Posição inválida")
