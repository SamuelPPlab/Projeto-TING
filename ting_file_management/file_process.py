from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if not instance.__len__():
        content = txt_importer(path_file)
        obj_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content
        }
        sys.stdout.write(f"{obj_info}\n")
        instance.enqueue(obj_info)
    else:
        pass


def remove(instance):
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')
    else:
        file_name = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f'Arquivo {file_name} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        search = instance.search(position)
        sys.stdout.write(f"{search}")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
