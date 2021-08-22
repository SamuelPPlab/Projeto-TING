import sys  # Referência: Luíse Rios


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")

    try:
        arquivo = open(path_file, 'r')
        texto = [linha for linha in arquivo.read().split("\n")]
        # essa ideia do read().split() foi da Luíse Rios
        arquivo.close()
        return texto
    except FileNotFoundError:
        sys.stderr.write(
            "Arquivo statics/arquivo_nao_existe.txt não encontrado\n"
            )
