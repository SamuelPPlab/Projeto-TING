from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if instance.__len__() == 0:
        response = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_importer(path_file)),
            "linhas_do_arquivo": txt_importer(path_file),
        }
        sys.stdout.write(f"{response}")
        return instance.enqueue(response)


def remove(instance):
    remove_from_file = instance.dequeue()
    if not remove_from_file:
        return sys.stdout.write("Não há elementos\n")
    else:
        file_name = remove_from_file["nome_do_arquivo"]
        return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    size = len(instance.data)
    if position >= size:
        return sys.stderr.write("Posição inválida\n")
    return instance.search(position)
