
def exists_word(word, instance):
    words = []
    files = []
    for index in range(len(instance)):
        file = instance.search(index)
        for line in file["linhas_do_arquivo"]:
            if word in line:
                words.append({"linha": index + 1})
        if len(words) > 0:
            word_file = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": words,
            }
            files.append(word_file)
    return files


def file_response(file, word, count):
    response = [{
        "ocorrencias": [count],
        "arquivo": f"{file}",
        "palavra": f"{word}"
    }]

    return response


def search_by_word(word, instance):
    response = list()
    file = instance.search(0)

    for count, words in enumerate(file['linhas_do_arquivo']):
        if(word.lower() in words.lower()):
            response = file_response(file['nome_do_arquivo'], word, {
                           'linha': count+1, 'conteudo': words})
    return response
