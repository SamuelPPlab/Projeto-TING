from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    file_lines = txt_importer(path_file)

    formated_data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_lines),
        'linhas_do_arquivo': file_lines,
    }

    if path_file not in instance.queue:
        instance.enqueue(path_file)

    sys.stdout.write(formated_data.__str__())
    return formated_data


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
