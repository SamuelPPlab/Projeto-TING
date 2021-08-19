import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    controler_duplicate = False

    for n in range(len(instance)):
        if instance.search(n)["nome_do_arquivo"] == result["nome_do_arquivo"]:
            controler_duplicate = True
            break

    if not controler_duplicate:
        instance.enqueue(result)

    sys.stdout.write(f'{result}\n')


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
