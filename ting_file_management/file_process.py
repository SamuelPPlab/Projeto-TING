import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance.__len__():
        file = txt_importer(path_file)
        data_file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }

        sys.stdout.write(f"{data_file}")
        instance.enqueue(data_file)
    else:
        pass


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")

    else:
        name = instance.search(0)["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {name} removido com sucesso\n")
        instance.dequeue()


def file_metadata(instance, position):
    try:
        file_position = instance.search(position)

        return sys.stdout.write(str(file_position))

    except IndexError:
        return sys.stderr.write("Posição inválida")
