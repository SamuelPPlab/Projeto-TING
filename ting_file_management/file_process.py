from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue


def process(path_file, instance):
    file_report = {
        'nome_do_arquivo': '',
        'qtd_linhas': '',
        'linhas_do_arquivo': ''
    }
    for i in range(len(instance)):
        if instance.search(i) == path_file:
            return False
    file_report['nome_do_arquivo'] = path_file
    file_report['linhas_do_arquivo'] = txt_importer(path_file)
    with open(path_file, 'r', newline='\n') as file:
        file_report["qtd_linhas"] = len(file.readlines())
    instance.enqueue(path_file)
    print(file_report)
    return True


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
        return False
    print(f'Arquivo {instance.search(1)} removido com sucesso')
    instance.dequeue()
    return True


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
