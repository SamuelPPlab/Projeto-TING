def exists_word(word, instance):
    for file in range(len(instance)):
        file_found = instance.search(file)
        texto = file_found["linhas_do_arquivo"]
        for palavra in texto:
            conta = palavra.lower().count(word.lower())
            if conta == 0:
                return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
