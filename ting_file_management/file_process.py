from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for element in range(len(instance)):
        if instance.search(element)["nome_do_arquivo"] == path_file:
            return None

    content_file = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content_file),
        "linhas_do_arquivo": content_file,
    }
    instance.enqueue(new_dict)
    sys.stdout.write(f"{new_dict}\n")


def remove(instance):
    try:
        path_file = None
        element_value = instance._head_value
        while element_value._next:
            element_value = element_value._next
        path_file = element_value._value["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
    except Exception:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    test_queue = Queue()
    process("statics/arquivo_teste.txt", test_queue)
    print("\n")
    # process("statics/nome_pedro.txt", test_queue)
    # print("\n")
    remove(test_queue)
    print("\n")
    remove(test_queue)
    print("\n")
    # print(test_queue)
