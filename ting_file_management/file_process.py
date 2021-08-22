import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance.find_file(path_file):
        data = txt_importer(path_file)
        instance.enqueue(path_file)

        lines = list()
        for line in data:
            lines.append(line)

        nr_of_lines = len(lines)

        sys.stdout.write(str({
            'nome_do_arquivo': path_file,
            'qtd_linhas': nr_of_lines,
            'linhas_do_arquivo': data
        }))


def remove(instance):
    if instance.__len__() < 1:
        return sys.stdout.write('Não há elementos\n')
    else:
        item = instance.dequeue()
        sys.stdout.write(f'Arquivo {item} removido com sucesso\n')


def file_metadata(instance, position):
    last_index = instance.__len__() - 1

    if position < 0 or position > last_index:
        return sys.stderr.write("Posição inválida\n")
