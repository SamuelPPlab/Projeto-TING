import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for row in range(0, instance.__len__()):
        if instance.search(row)["nome_do_arquivo"] == path_file:
            return None
    imported = txt_importer(path_file)
    output = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(imported),
        'linhas_do_arquivo': imported
    }
    try:
        instance.indexof(path_file)
    except ValueError:
        instance.enqueue(output)
    print(output)
    


def remove(instance):
    if(instance.__len__() == 0):
        return print('Não há elementos')
    removed = instance.dequeue()
    return print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        output = instance.search(position)
        return print(output)
    except IndexError:
        sys.stderr.write('Posição inválida')
