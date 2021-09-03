from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    """Aqui irá sua implementação"""
    added_files = []
    for item in instance.data:
        added_files.append(item['nome_do_arquivo'])
    if path_file not in added_files:
        new_file = txt_importer(path_file)
        info = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(new_file),
            'linhas_do_arquivo': new_file,
        }
        instance.enqueue(info)
        sys.stdout.write(f"{info}")

def remove(instance):
    """Aqui irá sua implementação"""
    added_files = instance.data
    if len(added_files) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        removed = instance.dequeue()
        sys.stdout.write(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso\n")

def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    length = len(instance.data)
    if length <= 0 or position >= length:
        sys.stderr.write('Posição inválida\n')
    else:
        result = instance.search(position)
        sys.stdout.write(str(result))
        