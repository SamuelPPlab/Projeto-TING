import sys
from ting_file_management.file_management import txt_importer


def process(file_path, instance):
    contents = txt_importer(file_path)
    output = {
        "nome_do_arquivo": file_path,
        "qtd_linhas": len(contents),
        "linhas_do_arquivo": contents
    }
    sys.stdout.write(f"{output}\n")
    instance.enqueue(output)

def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    rm_file = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {rm_file} removido com sucesso\n")

def file_metadata(instance, position):
    try:
        item = str(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
    else:
        sys.stdout.write(item)
