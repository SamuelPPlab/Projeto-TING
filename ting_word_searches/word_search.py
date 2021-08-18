def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result_list = list()
    for position in range(0, instance.__len__()):
        item = instance.search(position)
        matches = list()
        for line in item['linhas_do_arquivo']:
            if word.lower() in line.lower():
                matches.append({
                    'linha': item['linhas_do_arquivo'].index(line) + 1
                    })
        if len(matches) > 0:
            result_list.append({
                'palavra': word,
                'arquivo': item['nome_do_arquivo'],
                'ocorrencias': matches
            })
    return result_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    result_list = list()
    for position in range(0, instance.__len__()):
        item = instance.search(position)
        matches = list()
        for line in item['linhas_do_arquivo']:
            if word.lower() in line.lower():
                matches.append({
                    'linha': item['linhas_do_arquivo'].index(line) + 1,
                    'conteudo': line,
                })
        if len(matches) > 0:
            result_list.append({
                'palavra': word,
                'arquivo': item['nome_do_arquivo'],
                'ocorrencias': matches
            })
    return result_list
