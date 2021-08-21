import sys


def txt_importer(path_file):

    try:
        if path_file.endswith(".txt"):
            with open(path_file, "rt", newline="\n") as file_in:
                lines = []
                for line in file_in:
                    lines.append(line.strip())
                return lines
        else:
            return sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


# https://www.codegrepper.com/code-examples/python/reading+a+text+file+line+by+line+in+python
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
