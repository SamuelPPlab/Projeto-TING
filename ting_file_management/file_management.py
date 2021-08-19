import sys


def txt_importer(path_file):
    try:
        if path_file.endswith("txt"):
            with open(path_file, mode="r") as file:
                content = file.read()
                return content.split("\n")
        else:
            print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


if __name__ == "__main__":
    print(txt_importer("statics/arquivo_nao_existe.txt"))
