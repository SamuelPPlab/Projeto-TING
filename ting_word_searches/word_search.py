def exists_word(word, instance):
    found_word_list = []
    for index in range(len(instance)):
        file = instance.search(index)
        file_name = file['nome_do_arquivo']
        file_lines = file['linhas_do_arquivo']
        found_in_file_list = []

        for line_index, line in enumerate(file_lines):
            if (word.lower() in line.lower()):
                found_in_file_list.append({'linha': line_index + 1})

        if (len(found_in_file_list) != 0):
            found_word_list.append(
                {
                    'palavra': word,
                    'arquivo': file_name,
                    'ocorrencias': found_in_file_list,
                }
            )

    return found_word_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
