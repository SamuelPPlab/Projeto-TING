def exists_word(word, instance):
    occ = []
    for el in range(len(instance)):
        file = instance.search(el)

        current = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': []
        }

        for line in range(len(file['linhas_do_arquivo'])):
            if word in file['linhas_do_arquivo'][line]:
                current['ocorrencias'].append({'linha': line + 1})

        if len(current['ocorrencias']) > 0:
            occ.append(current)

    return occ


def search_by_word(word, instance):
    occ = []
    for el in range(len(instance)):
        file = instance.search(el)

        current = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': []
        }

        for line in range(len(file['linhas_do_arquivo'])):
            if word.lower() in file['linhas_do_arquivo'][line].lower():
                match = {
                    'linha': line + 1,
                    'conteudo': file['linhas_do_arquivo'][line]
                }
                current['ocorrencias'].append(match)

        if len(current['ocorrencias']) > 0:
            occ.append(current)

    return occ
