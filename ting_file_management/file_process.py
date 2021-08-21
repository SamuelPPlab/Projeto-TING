from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    if not instance.__len__():
        file_content = txt_importer(path_file)
        file_infos = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content
        }
        sys.stdout.write(f"{file_infos}\n")
        instance.enqueue(file_infos)
    else:
        pass


def remove(instance):
    """Aqui irá sua implementação"""
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')
    else:
        file = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f'Arquivo {file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        search = instance.search(position)
        sys.stdout.write(f"{search}")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
