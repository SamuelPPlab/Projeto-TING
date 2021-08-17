import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance:
        lines_from_file = txt_importer(path_file)
        data = {
            "nome do arquivo": path_file,
            "qtd_linhas": 3,
            "linhas_do_arquivo": lines_from_file
        }

        for file in instance.data:
            if file["nome do arquivo"] == path_file:
                return file


def remove(instance):
    if not instance:
        return print("Não há elementos", file=sys.stdout)
    
    removed_file = instance.dequeue()['nome do arquivo']
    print(f"Arquivo {removed_file} removido com sucesso", file=sys.stdout)



def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
