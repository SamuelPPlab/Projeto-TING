def exists_word(word, instance):
    data = list()
    for index in range(len(instance)):
        file_path = instance.search(index)
        file_data = {
            "palavra": word,
            "arquivo": file_path["nome_do_arquivo"],
            "ocorrencias": []
        }
        for row in file_path["linhas_do_arquivo"]:
            if word.lower() in row.lower():
                file_data["ocorrencias"].append({"linha": index + 1})

        if len(file_data["ocorrencias"]) > 0:
            data.append(file_data)
            print(file_data)
    return data

    # exists_word:
    # 1- iterar na instance
    # 2- em cada arquivo, iterar nas linhas do arquivo
    # 3- ver se a palavra está na linha
    # 4- se sim, criar uma lista com dict dentro. chave "linha" e add ao contador +1
    # 5- se não, passar para a próxima
    # 6- retornar lista com "palavra", "arquivo", "ocorrencias": [{"linha": 1}] 

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
