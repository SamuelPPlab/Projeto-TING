def exists_word(word, instance):
    words_info = []

    for index in range(instance.__len__()):
        file = instance.search(index)
        lines = file["linhas_do_arquivo"]
        occurrences = []

        count = 0
        for line in lines:
            count += 1
            if word.lower() in line.lower(): occurrences.append({'linha': count})

        if len(occurrences) > 0:
            words_info.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return words_info

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
