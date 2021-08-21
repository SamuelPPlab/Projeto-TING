
def exists_word(word, instance):
    files = instance.get_data()

    for item in files:
        if not any(word in w for w in item['linhas_do_arquivo']):
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    files = instance.get_data()

    for item in files:
        if not any(word in w for w in item['linhas_do_arquivo']):
            return []
