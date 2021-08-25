from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None

    file_lines = txt_importer(path_file)
    line_count = len(file_lines)

    data_to_queue = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": line_count,
        "linhas_do_arquivo": file_lines,
    }
    sys.stdout.write(f"{data_to_queue}/n")
    instance.enqueue(data_to_queue)


def remove(instance):
    if len(instance) > 0:
        file = instance.dequeue()
        return sys.stdout.write(f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n")
    return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    if 0 > position or position > len(instance):
        return sys.stderr.write("Posição inválida")
    return  sys.stdout.write(f"{instance.search(position)}")