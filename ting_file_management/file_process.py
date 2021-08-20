def process(path_file, instance):
    """Aqui irá sua implementação"""


def remove(instance):
    lengthInstance = len(instance)
    if lengthInstance > 0:
        excluirArquivo = instance.dequeue()
        print(f"Arquivo {excluirArquivo} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
