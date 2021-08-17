import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    lines = []
    try:
        new_var = check_file_type_in_path(path_file) != "txt"
        if new_var:
            sys.stderr.write("Formato inválido\n")
        else:
            with open(path_file, "rt", newline="\n") as f:
                for line in f:
                    lines.append(line.strip())
        return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


def check_file_type_in_path(path_file):
    return path_file.split(".")[1]


# if __name__ == "__main__":
#     print(txt_importer("statics/arquivo_test.txt"))
