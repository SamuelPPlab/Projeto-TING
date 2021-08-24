from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def exists_word(word, instance):
    current_file = instance.dequeue()

    lines = current_file.get("linhas_do_arquivo")

    occurrences = []

    for index, line in enumerate(lines):
        parsed_line = line.lower()
        parsed_word = word.lower()

        if parsed_word in parsed_line:
            occurrences.append({"linha": index + 1})

    if len(occurrences) == 0:
        return []

    return [
        {
            "palavra": word,
            "arquivo": current_file.get("nome_do_arquivo"),
            "ocorrencias": occurrences,
        }
    ]


def search_by_word(word, instance):
    current_file = instance.dequeue()

    lines = current_file.get("linhas_do_arquivo")

    occurrences = []

    for index, line in enumerate(lines):
        parsed_line = line.lower()
        parsed_word = word.lower()

        if parsed_word in parsed_line:
            occurrences.append({"linha": index + 1, "conteudo": line})

    if len(occurrences) == 0:
        return []

    return [
        {
            "palavra": word,
            "arquivo": current_file.get("nome_do_arquivo"),
            "ocorrencias": occurrences,
        }
    ]
