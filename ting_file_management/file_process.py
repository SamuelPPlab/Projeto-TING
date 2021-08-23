from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    conteudo = txt_importer(path_file)

    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    document = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(conteudo),
        "linhas_do_arquivo": conteudo
    }

    instance.enqueue(document)
    sys.stdout.write(f"{document}\n")


def remove(instance):
    if len(instance) > 0:
        removido = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f"Arquivo {removido} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        sys.stdout.write(f"{instance.search(position)}\n")
    except IndexError:
        sys.stderr.write("Posição inválida\n")

# if __name__ == "__main__":
#     lista = Queue()
#     process('statics/arquivo_teste.txt', lista)
#     print(process('statics/arquivo_teste.txt', lista))
#     # remove(lista)
#     file_metadata(lista, 2)
#     print(len(lista))
