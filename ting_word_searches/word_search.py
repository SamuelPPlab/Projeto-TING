def exists_word(word, instance):
    arquivo = instance.search(0)
    texto = arquivo["linhas_do_arquivo"]
    for palavra in texto:
        conta = palavra.lower().count(word.lower())
        if conta == 0:
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
