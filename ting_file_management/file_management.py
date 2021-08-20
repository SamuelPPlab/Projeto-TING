import sys


def txt_importer(path_file):
    if ".txt" in path_file:  # @MoisesSantana
        try:
            with open(path_file) as file:
                result = []
                for row in file:
                    result.append(row.strip())

                return result
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    return sys.stderr.write("Formato inválido\n")
