import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    try:
        instance.index(path_file)
    except ValueError:
        instance.enqueue(path_file)

    return print(
        f"'nome_do_arquivo': '{path_file}'\n",
        f"'qtd_linhas': {len(txt_importer(path_file))}'\n",
        f"'linhas_do_arquivo': {txt_importer(path_file)}'",
        file=sys.stdout,
    )


def remove(instance):
    try:
        return print(
            f"Arquivo {instance.dequeue()} removido com sucesso\n",
            file=sys.stdout,
        )
    except IndexError:
        return print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")
