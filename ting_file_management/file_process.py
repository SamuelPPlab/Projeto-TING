import sys
# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    content = txt_importer(path_file)
    current_queue = instance._data

    result = f"""'nome_do_arquivo': '{path_file}',
    'qtd_linhas': {len(content)},
    'linhas_do_arquivo': {content}"""

    if result not in current_queue:
        instance.enqueue(result)

    return sys.stdout.write(result)


def remove(instance):
    """Aqui irá sua implementação"""
    current_queue = instance._data
    if len(current_queue) == 0:
        return sys.stdout.write("Não há elementos\n")
    first_item = instance.dequeue()
    file_name = first_item.split(',')[0].split(" ")[1][1:-1]

    return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position > len(instance._data):
        return sys.stderr.write("Posição inválida\n")
    return sys.stdout.write(instance.search(position))

# q = Queue()
# process("statics/arquivo_teste.txt", q)
# remove(q)
