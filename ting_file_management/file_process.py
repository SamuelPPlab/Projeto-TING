import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    filenames = [file_data["nome_do_arquivo"] for file_data in instance._queue]

    if path_file not in filenames:
        file_data = {}
        file_data["nome_do_arquivo"] = path_file
        file_data["linhas_do_arquivo"] = txt_importer(path_file)
        file_data["qtd_linhas"] = len(file_data["linhas_do_arquivo"])
        instance.enqueue(file_data)

        print(
            f"'nome_do_arquivo': '{path_file}'\n",
            f"'qtd_linhas': {file_data['qtd_linhas']}\n",
            f"'linhas_do_arquivo': {file_data['linhas_do_arquivo']}",
        )


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    file_path = instance.dequeue()["nome_do_arquivo"]
    print(
        f"Arquivo {file_path} removido com sucesso\n",
        file=sys.stdout,
    )


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
