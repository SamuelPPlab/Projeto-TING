def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = list()
    for file in instance.queue:
        find = False
        lines = list()
        for row in file['linhas_do_arquivo']:
            if word.lower() in row.lower():
                find = True
                lines.append({ 'linha': file['linhas_do_arquivo'].index(row) + 1 })

        if find:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': lines
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
