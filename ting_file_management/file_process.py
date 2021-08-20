import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):

    objectRes = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    if instance.existResult(objectRes) == True:
        return None

    instance.enqueue(objectRes)

    result = print(objectRes, file=sys.stdout)

    return result


def remove(instance):
    lengthInstance = len(instance)
    if lengthInstance > 0:
        excludPath = instance.dequeue()
        print(
            f"Arquivo {excludPath['nome_do_arquivo']} removido com sucesso\n",
            file=sys.stdout,
        )
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        arquivo = instance.search(position)
        print(arquivo, file=sys.stdout)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
