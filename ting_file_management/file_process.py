import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    content = txt_importer(path_file)
    current_queue = instance._data

    if content not in current_queue:
        instance.enqueue(content)

    result = f"""'nome_do_arquivo': '{path_file}',
    'qtd_linhas': {len(content)},
    'linhas_do_arquivo': {content}"""

    return sys.stdout.write(result)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
