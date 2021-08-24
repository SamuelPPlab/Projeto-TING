import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return ""

    txt_value = txt_importer(path_file)

    response = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_value),
        "linhas_do_arquivo": txt_value,
    }

    print(response)
    instance.enqueue(response)


def remove(instance):
    try:
        dequeueValue = instance.dequeue()
        print(
            f"Arquivo {dequeueValue['nome_do_arquivo']} removido com sucesso"
            )
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
