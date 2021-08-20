import sys
from ting_file_management.file_management import txt_importer


def generate_report(path_file):
    file = txt_importer(path_file)
    file_report = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
    print(file_report)


def load_queue(instance):
    return [instance.search(index) for index in range(len(instance))]


def process(path_file, instance):
    queue = load_queue(instance)

    if path_file not in queue:
        instance.enqueue(path_file)
        generate_report(path_file)


def remove(instance):
    if len(instance) > 0:
        removed_path = instance.dequeue()
        print(f"Arquivo {removed_path} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    if len(instance) <= position:
        print('Posição inválida', file=sys.stderr)
    else:
        path = instance.search(position)
        generate_report(path)
