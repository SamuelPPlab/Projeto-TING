import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance.__len__():
        text_content = txt_importer(path_file)
        text_preprocessed = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_content),
            "linhas_do_arquivo": text_content,
        }
        sys.stdout.write(f"{text_preprocessed}\n")
        instance.enqueue(text_preprocessed)
    else:
        pass


def remove(instance):
    if not instance:
        return print("Não há elementos", file=sys.stdout)

    removed_file = instance.dequeue()['nome do arquivo']
    print(f"Arquivo {removed_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
