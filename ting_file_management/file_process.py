import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    my_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    sys.stdout.write(f"{my_dict}")
    instance.enqueue(my_dict)


def remove(instance):
    try:
        file = instance.search(0)['nome_do_arquivo']
        sys.stdout.write(f"Arquivo {file} removido com sucesso\n")
        instance.dequeue()
    except Exception:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(f"{instance.search(position)}")
    except Exception:
        sys.stderr.write("Posição inválida\n")
