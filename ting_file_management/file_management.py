import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")
        with open(path_file, "r", encoding="utf-8") as file:
            lista = []
            for item in file:
                lista.append(item.strip())
            return lista

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


if __name__ == "__main__":
    print(txt_importer("statics/arquivo_teste.txt"))
