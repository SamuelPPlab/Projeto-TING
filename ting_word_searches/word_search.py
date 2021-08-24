def exists_word(word, instance):
    for i in instance:
        content = ''
        for index in i['linhas_do_arquivo'][0]:
            content += index
        quantity_found = content.count(word)
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

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
