import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """
        - Se nome de arquivo já existe em queue, ignora
        - Importa dados do arquivo com função txt_importer
        - Conta quantidade de linhas
        - Adiciona um objeto à fila com:
            -"nome_do_arquivo", "qtd_linhas" e "linhas_do_arquivo"
        - Saída via stdout(sys) para cada adição válida
    """
    # Ref: Moisés Santana
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None
    file = txt_importer(path_file)
    lenght = len(file)
    file_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lenght,
        "linhas_do_arquivo": file,
    }
    instance.enqueue(file_content)
    sys.stdout.write(f"{file_content}")


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        file_removed = instance.dequeue()
        print(
            f"Arquivo {file_removed['nome_do_arquivo']} removido com sucesso"
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
