from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if len(instance) == 0:
        txt_content = txt_importer(path_file)
        line_counter = len(txt_content)

        result = {
                "nome_do_arquivo": path_file,
                "qtd_linhas": line_counter,
                "linhas_do_arquivo": txt_content,
            }

        instance.enqueue(result)

        # tip from @luise-rios
        sys.stdout.write(f"{result}")


def remove(instance):
    try:
        dequeued_file = instance.dequeue()['nome_do_arquivo']
        print(f"Arquivo {dequeued_file} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
