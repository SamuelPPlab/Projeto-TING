# from collections import deque
from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def sliding_window(string: str, window_size: int):
    window_limit = len(string) - window_size + 1
    for window_init in range(window_limit):
        window_end = window_init + window_size
        yield tuple(string[window_init:window_end])


def exists_word(word, instance):

    occurrences_list = []

    for item in instance:
        result = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line_index, line_word in enumerate(item["linhas_do_arquivo"], 1):
            occurrences = sliding_window(line_word, len(word))

            if tuple(word) in occurrences:
                result["ocorrencias"].append({"linha": line_index})

        if result["ocorrencias"]:
            occurrences_list.append(result)

    return occurrences_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
