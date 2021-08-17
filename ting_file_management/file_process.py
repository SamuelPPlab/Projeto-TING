import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None

    file_in_arr = txt_importer(path_file)
    result_qty_row = len(file_in_arr)
    instance.enqueue({
        "nome_do_arquivo": path_file,
        "qtd_linhas": result_qty_row,
        "linhas_do_arquivo": file_in_arr
    })

    print(instance.search(len(instance) - 1))


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        print('Não há elementos')
    else:
        removed_element = instance.dequeue()
        file_name = removed_element['nome_do_arquivo']
        print(f'Arquivo {file_name} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if 0 <= position < len(instance):
        print(instance.search(position))
    else:
        sys.stderr.write('Posição inválida')
