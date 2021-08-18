import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    nome_do_arquivo = path_file
    qtd_linhas = len(txt_importer(path_file))
    linhas_do_arquivo = txt_importer(path_file)
    process_content = {
        "nome_do_arquivo": nome_do_arquivo,
        "qtd_linhas": qtd_linhas,
        "linhas_do_arquivo": linhas_do_arquivo,
    }
    if len(instance) > 0:
        last_file = instance.search(len(instance) - 1)
        if last_file["nome_do_arquivo"] != nome_do_arquivo:
            instance.enqueue(process_content)
    else:
        instance.enqueue(process_content)

    return sys.stdout.write(str(process_content))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    file_to_remove = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    return sys.stdout.write(f"Arquivo {file_to_remove} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        _ = instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")
