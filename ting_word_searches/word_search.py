def exists_word(word, instance):
    results = []

    for file_path in instance._data:
        info = {}

        info['arquivo'] = file_path['nome_do_arquivo']
        info['ocorrencias'] = []

        for i, row in enumerate(file_path['linhas_do_arquivo']):
            if word.lower() in row.lower():
                info['palavra'] = word
                info['ocorrencias'].append({'linha': i + 1})

        if len(info['ocorrencias']):
            results.append(info)

    return results


def search_by_word(word, instance):
    results = []

    for file_path in instance._data:
        info = {}

        info['arquivo'] = file_path['nome_do_arquivo']
        info['ocorrencias'] = []

        for i, row in enumerate(file_path['linhas_do_arquivo']):
            if word.lower() in row.lower():
                info['palavra'] = word
                info['ocorrencias'].append({'linha': i + 1, 'conteudo': row})

        if len(info['ocorrencias']):
            results.append(info)

    return results
