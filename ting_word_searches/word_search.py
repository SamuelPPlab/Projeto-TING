def exists_word(word, instance):
    word_found = list()

    for file in range(len(instance)):
        file_found = instance.search(file)
        lines_found = file_found["linhas_do_arquivo"]

        occurrences = []
        for line in lines_found:
            counter = 0
            if word.lower() in line.lower():
                counter += 1
                occurrences.append({"linha": counter})

            if len(occurrences) > 0:
                word_found.append(
                    {
                        "palavra": word,
                        "arquivo": file_found["nome_do_arquivo"],
                        "ocorrencias": occurrences,
                    }
                )
    return word_found


def search_by_word(word, instance):
    word_found = list()

    for file in range(len(instance)):
        file_found = instance.search(file)
        lines_found = file_found["linhas_do_arquivo"]

        occurrences = []
        for line in lines_found:
            counter = 0
            if word.lower() in line.lower():
                counter += 1
                occurrences.append({"linha": counter, "conteudo": line})

            if len(occurrences) > 0:
                word_found.append(
                    {
                        "palavra": word,
                        "arquivo": file_found["nome_do_arquivo"],
                        "ocorrencias": occurrences,
                    }
                )
    return word_found
