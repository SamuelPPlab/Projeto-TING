# def verificar_arquivo():

def txt_importer(path_file):
    resp = []
    try:    
        with open(path_file, "r") as f:
            contents = f.readlines()
            for index in contents:
                resp.append(index.strip())
    except FileNotFoundError:
        return Exception(f"Arquivo {path_file} não encontrado")
    else:
        return resp

print(txt_importer("../statics/arquivo_teste.txt"))