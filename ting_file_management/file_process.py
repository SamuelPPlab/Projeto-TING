from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if len(instance) < 1:
        file = txt_importer(path_file)
        resuslt = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }

        sys.stdout.write(str(resuslt))
        instance.enqueue(resuslt)


def remove(instance):
    if len(instance) <= 0:
        return sys.stdout.write("Não há elementos\n")

    file_removed = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_removed} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return file

    except IndexError:
        sys.stderr.write("Posição inválida\n")
