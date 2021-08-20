def exists_word(word, instance):
    resultados = []

    for index in range(len(instance)):
        event = []
        file = instance.search(index)
        lines = file['linhas_do_arquivo']
        counter = 0
        for line in lines:
            counter += 1
            if word in line:
                event.append({'linha': counter})

        if len(event) > 0:
            details = {}
            details['palavra'] = word
            details['arquivo'] = file['nome_do_arquivo']
            details['ocorrencia'] = event
            resultados.append(details)

    return resultados


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
