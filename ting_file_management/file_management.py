import sys
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
# def verificar_arquivo():


def txt_importer(path_file):
    resp = []
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as f:
            contents = f.readlines()
            for index in contents:
                resp.append(index.strip())
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        return resp

# print(txt_importer("../sttics/arquivo_teste.txt"))
# print(txt_importer("../statics/arquivo_teste.txt"))
