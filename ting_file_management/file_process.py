from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if instance.__len__():
        pass
    else:
        content = txt_importer(path_file)
        lines = len(content)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": lines,
            "linhas_do_arquivo": content,
        }
        instance.enqueue(data)
        sys.stdout.write(f"{data}")


def remove(instance):
    if not len(instance):
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.search(0)["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
        instance.dequeue()


def file_metadata(instance, position):
    if position < 0:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
    else:
        sys.stderr.write("Posição inválida")
