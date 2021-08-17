import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    content = txt_importer(path_file)
    current_queue = instance._data

    result = f"""'nome_do_arquivo': '{path_file}',
    'qtd_linhas': {len(content)},
    'linhas_do_arquivo': {content}"""

    file_names = [
        item["nome_do_arquivo"]
        for item in current_queue if item["nome_do_arquivo"] == path_file]
    if len(file_names) == 0:
        instance.enqueue({
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content
        })

    return sys.stdout.write(result)


def remove(instance):
    """Aqui irá sua implementação"""
    current_queue = instance._data
    if len(current_queue) == 0:
        return sys.stdout.write("Não há elementos\n")
    first_item = instance.dequeue()
    file_name = first_item["nome_do_arquivo"]

    return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position > len(instance._data):
        return sys.stderr.write("Posição inválida\n")
    item = instance.search(position)
    result = f"""'nome_do_arquivo': '{item["nome_do_arquivo"]}',
    'qtd_linhas': {len(item["linhas_do_arquivo"])},
    'linhas_do_arquivo': {item["linhas_do_arquivo"]}"""
    return sys.stdout.write(result)
