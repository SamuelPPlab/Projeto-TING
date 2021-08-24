def exists_word(word, instance):
    for i in instance:
        quantity_found = sum_of_occurrences(word, i)
        if quantity_found == 0:
            return []
        return [{
            'palavra': word,
            'arquivo': i['nome_do_arquivo'],
            'ocorrencias': [
                {
                    'linha': quantity_found,
                }
            ],
        }]


def sum_of_occurrences(word, index):
    content = ''
    for i in index['linhas_do_arquivo'][0]:
        content += i
    quantity_found = content.count(word)
    return quantity_found


def search_by_word(word, instance):
    for i in instance:
        quantity_found = sum_of_occurrences(word, i)
        if quantity_found == 0:
            return []
        for index in i['linhas_do_arquivo'][0]:
            content = ''
            content += index
            return [{
                'palavra': word,
                'arquivo': i['nome_do_arquivo'],
                'ocorrencias': [
                    {
                        'linha': sum_of_occurrences(word, index),
                        "conteudo": content,
                    }
                ],
                }]
