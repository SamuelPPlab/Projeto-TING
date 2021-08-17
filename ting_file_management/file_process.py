import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__():
        pass
    else:
        text = txt_importer(path_file)
        lines_number = len(text)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": lines_number,
            "linhas_do_arquivo": text,
        }
        instance.enqueue(result)
        sys.stdout.write(f"{result}")


def remove(instance):
    if not len(instance):
        sys.stdout.write("Não há elementos\n")
    else:
        file_name = instance.search(0)["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")
        instance.dequeue()


def file_metadata(instance, position):
    if position < 0:
        file_name = instance.search(position)
        sys.stdout.write(f"{file_name}")
    else:
        sys.stderr.write("Posição inválida")
