import sys
from ting_file_management.file_management import txt_importer


# instance = instância da classe


def process(path_file, instance):
    value = {}
    for elem in instance._data:
        if path_file == elem["nome_do_arquivo"]:
            return

    lines = txt_importer(path_file)
    lines_qtd = len(lines)

    value["nome_do_arquivo"] = path_file
    value["qtd_linhas"] = lines_qtd
    value["linhas_do_arquivo"] = lines

    instance.enqueue(value)
    return sys.stdout.write(f"{value}\n")


def remove(instance):
    if len(instance._data) > 0:
        arquivo = instance.dequeue()
        nome_arquivo = arquivo["nome_do_arquivo"]
        return sys.stdout.write(
            f"Arquivo {nome_arquivo} removido com sucesso\n"
            )
    else:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        informacoes = instance.search(position)
        return informacoes
    except IndexError:
        return sys.stderr.write("Posição inválida")
