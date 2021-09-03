from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if not len(instance):
        file = txt_importer(path_file)
        content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
        instance.enqueue(content)
        sys.stdout.write(f"{content}")


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    path = instance.search(0)["nome_do_arquivo"]
    return print(
        f'Arquivo {path} removido com sucesso'
    )


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        sys.stderr.write('Posição inválida')
