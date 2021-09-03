import sys


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    data = instance.data
    results = []
    for item in data:
        placeholder = { 'arquivo': item['nome_do_arquivo'], 'ocorrencias': [], 'palavra': word }
        for index, linha in enumerate(item['linhas_do_arquivo']):
            lower_l = linha.lower()
            lower_w = word.lower()
            if lower_w in lower_l:
                placeholder['ocorrencias'].append({'linha': index + 1})
        results.append(placeholder)
    if len(results[0]['ocorrencias']) > 0:
        return results
    return []

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
