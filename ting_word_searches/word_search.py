def exists_word(word, instance):
    file = instance.search(0)
    file_name = file['nome_do_arquivo'].lower()
    if word.lower() in file_name:
        dict_babado = dict()
        return dict_babado
    else:
        return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
