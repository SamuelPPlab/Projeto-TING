import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    for item in range(0, instance.__len__()):
        if path_file == instance.search(item)["nome_do_arquivo"]:
            return None
    objeto = {
        "nome_do_arquivo": path_file,              # Nome do arquivo recém adicionado
        "qtd_linhas": len(file),                   # Quantidade de linhas existentes no arquivo
        "linhas_do_arquivo": file                  # linhas retornadas pela função do requisito 2
    }

    sys.stdout.write(f"{objeto}\n")
    return instance.enqueue(objeto)


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    tirou = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {tirou} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")


if __name__ == "__main__":
    project = Queue()
    process("statics/arquivo_teste.txt", project)
    process("statics/arquivo_teste.txt", project)
