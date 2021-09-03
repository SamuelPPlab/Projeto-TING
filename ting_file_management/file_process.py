from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    """Aqui irá sua implementação"""
    if not len(instance):
        new_file = txt_importer(path_file)
        info = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(new_file),
            'linhas_do_arquivo': new_file,
        }
        instance.enqueue(info)
        sys.stdout.write(f"{info}")

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
