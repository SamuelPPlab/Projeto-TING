import sys


def txt_importer(path_file):

    """Aqui irá sua implementação"""
    file_extension = path_file.split(".")[1]
    try:
        if file_extension != "txt":
            return sys.stderr.write("Formato inválido\n")
        else:
            txt_content = []
            with open(path_file, 'r') as txt_file:
                file = txt_file.readlines()
                for line in file:
                    txt_content.append(line.strip())
                print(txt_content)
                return txt_content

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        return file
