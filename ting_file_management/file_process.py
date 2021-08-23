from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    process_dict = {}
    txt = txt_importer(path_file)
    process_dict['nome_do_arquivo'] = path_file
    process_dict['qtd_linhas'] = len(txt)
    process_dict['linhas_do_arquivo'] = txt
    print(process_dict)
    instance.enqueue(process_dict)


def remove(instance):
    """"""


def file_metadata(instance, position):
    """"""
