import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    if instance.file_already_exists(file_process):
        return None

    instance.enqueue(file_process)

    return print(
        f"'nome_do_arquivo': '{path_file}'\n",
        f"'qtd_linhas': {len(txt_importer(path_file))}'\n",
        f"'linhas_do_arquivo': {txt_importer(path_file)}'",
        file=sys.stdout,
    )


def remove(instance):
    try:
        exclude = instance.dequeue()
        return print(
            f"Arquivo {exclude['nome_do_arquivo']} removido com sucesso\n",
            file=sys.stdout,
        )
    except IndexError:
        return print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")
