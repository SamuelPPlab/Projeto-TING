import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)

    for item in instance.getAll():
        if (item['nome do arquivo'] == path_file):
            return None

    exit_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "Linhas_do_arquivo": content
    }

    instance.enqueue(exit_file)
    return sys.stdout.write(f"{exit_file}\n")


def remove(instance):
    if not instance:
        return print("Não há elementos", file=sys.stdout)

    removed_file = instance.dequeue()['nome do arquivo']
    print(f"Arquivo {removed_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
