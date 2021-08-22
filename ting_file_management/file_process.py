import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    news = txt_importer(path_file)
    if instance.search_by_value(path_file) < 1:
        file_data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(news),
            'linhas_do_arquivo': news,
        }
        instance.enqueue(file_data)
        sys.stdout.write(str(file_data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
