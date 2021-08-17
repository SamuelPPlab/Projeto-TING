import sys


def txt_importer(path_file):
    """
        - Importa informações de um arquivo .txt, tendo "\n" como separador.
    """

    try:
        if path_file.endswith(".txt"):
            with open(path_file) as content_file:
                return [line for line in content_file.read().strip().split(
                    "\n")]
        else:
            return sys.stderr.write("Formato inválido\n")

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
