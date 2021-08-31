import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    data = txt_importer(path_file)
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    if len(instance) > 0:
        last_file = instance.search(len(instance) - 1)
        if last_file["nome_do_arquivo"] != path_file:
            instance.enqueue(output)
    else:
        instance.enqueue(output)

    return sys.stdout.write(str(output))


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    file_to_remove = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    return sys.stdout.write(f"Arquivo {file_to_remove} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        _ = instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")
