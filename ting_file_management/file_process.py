import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i) == path_file:
            print(instance.search(i))
            return False
    print(get_file_report(path_file, instance))
    instance.enqueue(path_file)
    return True


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
        return False
    print(f'Arquivo {instance.search(1)} removido com sucesso')
    instance.dequeue()
    return True


def file_metadata(instance, position):
    try:
        file_path = instance.search(position)
        process(file_path, instance)
        return True
    except(IndexError):
        sys.stderr.write('Posição inválida')


def get_file_report(path_file, instance):
    file_report = {
        'nome_do_arquivo': '',
        'qtd_linhas': '',
        'linhas_do_arquivo': ''
    }
    file_report['nome_do_arquivo'] = path_file
    file_report['linhas_do_arquivo'] = txt_importer(path_file)
    with open(path_file, 'r', newline='\n') as file:
        file_report["qtd_linhas"] = len(file.readlines())
    return file_report
