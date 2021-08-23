def exists_word(word, instance):
    overall = []
    queue = instance.my_queue
    for item in queue:
        item_dict = {
            'palavra': word,
            'arquivo': item['nome_do_arquivo']
        }
        appears = []
        index = 1
        for line in item['linhas_do_arquivo']:
            if (line.lower()).find(word.lower()) != -1:
                line_dict = {
                    'linha': index
                }
                appears.append(line_dict)
            index += 1
        item_dict['ocorrencias'] = appears
        overall.append(item_dict)
    if len(appears) == 0:
        return []
    else:
        return overall


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
