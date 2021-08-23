import sys
from ting_file_management.file_management import txt_importer


def find_file(path_file, instance):
    return path_file in instance.files


def process(path_file, instance):
    if not find_file(path_file, instance):
        file_content = txt_importer(path_file)
        instance.enqueue(path_file)
        lines = list()
        for line in file_content:
            lines.append(line)
        lines_count = len(lines)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": lines_count,
            "linhas_do_arquivo": file_content
        }

        sys.stdout.write(str(result))


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    file = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {file} removido com sucesso\n"
    )


def file_metadata(instance, position):
    if position > instance.__len__() - 1:
        return sys.stderr.write("Posição inválida\n")
    else:
        file = instance.search(position)
        return sys.stdout.write(str(file))
