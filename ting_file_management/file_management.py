def txt_importer(path_file):
    try:
        with open(path_file, "r", encoding="utf-8") as file:
            content_file = []
            if path_file.split('.')[-1] == 'txt':                
                for readline in file:
                    content_file.append(readline.rstrip('\n'))
                return content_file
            return "Formato inválido\n"
    except:
        return f"Arquivo {path_file} não encontrado\n"

print(txt_importer("statics/arquivo_teste.txt"))

print(txt_importer("statics/arquivo_teste.csv"))

print(txt_importer("statics/arquivo_nao_existe.txt"))