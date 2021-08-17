import sys


def txt_importer(path_file):
    try:
        document_type = path_file[-3:]
        if document_type != "txt":
            # https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
            return sys.stderr.write("Formato inválido\n")
        with open(path_file, mode="r") as file:
            my_list = list()
            content = file.read()
            split_phrases = content.split("\n")
            for words in split_phrases:
                my_list.append(words)
            return my_list
    except FileNotFoundError:
        # https://cadernoscicomp.com.br/tutorial/introducao-a-programacao-em-python-3/tratamento-de-erros-e-excecoes/
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
