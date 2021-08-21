from ting_file_management.file_process import file_metadata


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    wordlower = word.lower()
    occurrences = []
    for i in range(len(instance)):
        metadata = file_metadata(instance, i)
        occurrences_in_this_file = [
            {"linha": i + 1}
            for i, line in enumerate(metadata["linhas_do_arquivo"])
            if wordlower in line.lower()
        ]
        if occurrences_in_this_file:
            occurrences.append({
                "palavra": word,
                "arquivo": metadata["nome_do_arquivo"],
                "ocorrencias": occurrences_in_this_file
            })
    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    wordlower = word.lower()
    occurrences = []
    for i in range(len(instance)):
        metadata = file_metadata(instance, i)
        occurrences_in_this_file = [
            {
                "linha": i + 1,
                "conteudo": line
            }
            for i, line in enumerate(metadata["linhas_do_arquivo"])
            if wordlower in line.lower()
        ]
        if occurrences_in_this_file:
            occurrences.append({
                "palavra": word,
                "arquivo": metadata["nome_do_arquivo"],
                "ocorrencias": occurrences_in_this_file
            })
    return occurrences
