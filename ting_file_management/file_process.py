from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    index = 0
    can_process = True
    while index < instance.__len__():
        if path_file == instance.search(index)["nome_do_arquivo"]:
            can_process = False
            break
    if can_process:
        data_file = txt_importer(path_file)

        processed_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data_file),
            "linhas_do_arquivo": data_file,
        }
        instance.enqueue(processed_data)
        sys.stdout.write(f"{processed_data}")


def remove(instance):
    if not instance.__len__():
        sys.stdout.write("Não há elementos\n")
    else:
        file_to_remove = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {file_to_remove} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
