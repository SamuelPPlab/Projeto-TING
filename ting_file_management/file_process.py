import sys
from ting_file_management.file_management import txt_importer


def build(path_file):
    content = txt_importer(path_file)
    return {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }


def process(path_file, instance):
    try:
        if instance.__len__():
            raise ValueError()
        else:
            content_file = build(path_file)
            sys.stdout.write(f"{content_file}\n")
            instance.enqueue(content_file)
    except ValueError:
        print('Posição inválida', file=sys.stderr)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
