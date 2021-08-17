import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    if len(instance) < 1:
        file = txt_importer(path_file)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
        sys.stdout.write(str(result))
        instance.enqueue(result)

def remove(instance):
    file_length = len(instance)
    if file_length <= 0:
        return sys.stdout.write("Não há elementos\n")
    removed_file = instance.dequeue()['nome_do_arquivo']
    sys.stdout.write(f"Arquivo {removed_file} removido com sucesso\n")



def file_metadata(instance, position):
    try:
        search_result = instance.search(position)
        return sys.stdout.write(str(search_result))
    except IndexError:
        sys.stderr.write("Posição inválida")
