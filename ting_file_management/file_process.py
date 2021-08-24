import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file = txt_importer(path_file)
    format_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    sys.stdout.write(str(format_data))
    instance.enqueue(format_data)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    item_removed = instance.dequeue()
    file_removed = item_removed["nome_do_arquivo"]
    return sys.stdout.write(
        f"Arquivo {file_removed} removido com sucesso\n"
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position > len(instance):
        return sys.stderr.write("Posição inválida\n")
    process_file = instance.search(position)
    return sys.stdout.write(f"{process_file}")
