from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    new_txt = txt_importer(path_file)
    for index in range(instance.__len__()):
        if instance.search(index)["nome_do_arquivo"] == path_file: return None

    lines = len(new_txt)
    infos = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lines,
        "linhas_do_arquivo": new_txt
    }

    instance.enqueue(infos)
    sys.stdout.write(str(infos))


def remove(instance):
    if instance.__len__() > 0:
        file = instance.dequeue()
        return sys.stdout.write(f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n")
    return sys.stdout.write("Não há elementos\n")

def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida\n")