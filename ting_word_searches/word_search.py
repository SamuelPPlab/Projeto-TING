

def build(file, word, count):
    result = [{
        "palavra": f"{word}",
        "arquivo": f"{file}",
        "ocorrencias": [count]
    }]
    return result


def exists_word(word, instance):
    result = list()
    file = instance.search(0)
    for count, words in enumerate(file['linhas_do_arquivo']):
        if(word.lower() in words.lower()):
            result = build(file['nome_do_arquivo'], word, {'linha': count+1})
    return result


def search_by_word(word, instance):
    result = list()
    file = instance.search(0)
    for count, words in enumerate(file['linhas_do_arquivo']):
        if(word.lower() in words.lower()):
            result = build(file['nome_do_arquivo'], word, {
                           'linha': count+1, 'conteudo': words})
    return result
