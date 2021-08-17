from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    my_data = dict()
    data_len = len(txt_importer(path_file))
    my_data["nome_do_arquivo"] = path_file
    my_data["qtd_linhas"] = data_len
    my_data["linhas_do_arquivo"] = txt_importer(path_file)
    # https://stackoverflow.com/questions/4547274/convert-a-python-dict-to-a-string-and-back
    to_str = str(my_data)
    # https://www.geeksforgeeks.org/sys-stdout-write-in-python/
    return sys.stdout.write(to_str)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# teste = process("statics/arquivo_teste.txt", "oi")
# print(teste)
