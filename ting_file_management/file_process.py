from ting_file_management.file_management import txt_importer
import sys


def search_by_file_name(data, path_file):
    for name in data:
        if(name['nome_do_arquivo'] == path_file):
            return True
        return False


def process(path_file, instance):
    data = instance.get_data()
    if search_by_file_name(data, path_file):
        return 1
    process_file = {}
    file = txt_importer(path_file)
    process_file['nome_do_arquivo'] = path_file
    process_file['qtd_linhas'] = len(file)
    process_file['linhas_do_arquivo'] = file
    instance.enqueue(process_file)
    sys.stdout.write(f"{process_file}\n")
    return process_file


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    file_removed = instance.dequeue()
    name_file = file_removed.get('nome_do_arquivo')
    return sys.stdout.write(f" Arquivo {name_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        return sys.stderr.write('Posição inválida')

# references
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
