import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__() < 1:
        txt_file = txt_importer(path_file)
        to_write = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_file),
            "linhas_do_arquivo": txt_file
        }
        sys.stdout.write(str(to_write))
        return instance.enqueue(to_write)


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() > 0:
        new_lista = instance.dequeue()
        print(f"Arquivo {new_lista['nome_do_arquivo']} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if 0 <= position < instance.__len__():
        return instance.search(position)
    else:
        sys.stderr.write("Posição inválida\n")
