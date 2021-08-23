import sys
def txt_importer(path_file):
    if not (path_file.endswith(".txt")):
        return print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, mode="r") as file:
            lines = [line.rstrip('\n') for line in file]
            return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado",file=sys.stderr )

# https://qastack.com.br/programming/3277503/how-to-read-a-file-line-by-line-into-a-lists