from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    for item in range(0, instance.__len__()):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(result)

    print(result)


def remove(instance):
    item = instance.dequeue()
    if not item:
        return print("Não há elementos")
    return print(f"Arquivo {item['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        return print(item)
    except IndexError:
        sys.stderr.write("Posição inválida")


# Source: Anderson Alves / Emerson Junqueira