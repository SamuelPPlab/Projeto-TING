import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance.__len__():
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_importer(path_file)),
            "linhas_do_arquivo": txt_importer(path_file),
        }
        instance.enqueue(data)
        sys.stdout.write(f"{data}")


def remove(instance):
    if instance.__len__():
        path_file = instance.search(0)["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
        instance.dequeue()
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    if position < 0:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
    else:
        sys.stderr.write("Posição inválida")
