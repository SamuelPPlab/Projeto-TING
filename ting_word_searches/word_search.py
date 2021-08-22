def exists_word(word, instance):
    word_found = [{
        'palavra': word,
        'arquivo': '',
        'ocorrencias': [],
    }]
    for instance_len in range(len(instance)):
        file = instance.search(instance_len)
        word_found[0]['arquivo'] = file['nome_do_arquivo']
        ocurrencies_found = word_found[0]['ocorrencias']

        for index, line in enumerate(file['linhas_do_arquivo']):
            if word in line:
                ocurrencies_found.append({'linha': index + 1})
        if len(ocurrencies_found) > 0:
            return word_found
        else:
            return ocurrencies_found


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
