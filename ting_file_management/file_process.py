import sys
from ting_file_management.file_management import txt_importer

# Adiciona (enqueue da classe criada anteriormente)
# Não sei se entendi bem o requisito quando é dito que deve ignorar arquivos
# com o mesmo nome, mas aparentemente é pra verificar se já existe um
# arquivo processado e evitar duplicar, mas não tenho certeza


def process(path_file, instance):
    for item in instance.queue:
        if item["nome_do_arquivo"] == path_file:
            return None
    txt = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    instance.enqueue(result)
    sys.stdout.write(f"{result}\n")


# Remove (dequeue da classe criada anteriormente)


def remove(instance):
    if not instance.__len__():
        return sys.stdout.write("Não há elementos\n")
    result = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {result} removido com sucesso\n")


# Faz a busca pelo index (search da classe criada anteriormente)


def file_metadata(instance, position):
    if position in range(instance.__len__()):
        result = instance.search(position)
        return sys.stdout.write(str(result))
    sys.stderr.write("Posição inválida\n")
