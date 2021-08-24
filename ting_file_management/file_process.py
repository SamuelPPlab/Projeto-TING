import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for file in range(len(instance)):
        if instance.search(file)['nome_do_arquivo'] == path_file:
            return None

    file = txt_importer(path_file)
    pre_process_result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    sys.stdout.write(f"{pre_process_result}")
    instance.enqueue(pre_process_result)


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    else:
        file = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f"Arquivo {file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
    except IndexError:
        sys.stderr.write("Posição inválida\n")

# https://www.geeksforgeeks.org/sys-stdout-write-in-python/
# Rafael M Guimarães
