from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if path_file not in instance.my_file_names:
        process_dict = {}
        txt = txt_importer(path_file)
        process_dict["nome_do_arquivo"] = path_file
        process_dict["qtd_linhas"] = len(txt)
        process_dict["linhas_do_arquivo"] = txt
        instance.enqueue(process_dict)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        name = instance.my_queue[0]["nome_do_arquivo"]
        print(f"Arquivo {name} removido com sucesso")
        instance.dequeue()


def file_metadata(instance, position):
    try:
        print(instance.my_queue[position])
    except IndexError:
        print("Posição inválida", file=sys.stderr)
