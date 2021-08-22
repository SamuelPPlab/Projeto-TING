from collections import deque


def sliding_window(string: str, window_size: int):
    window_limit = len(string) - window_size + 1
    for window_init in range(window_limit):
        window_end = window_init + window_size
        yield deque(string[window_init:window_end])


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

            if deque(word) in occurrences:
                result["ocorrencias"].append({"linha": line_index})

        if result["ocorrencias"]:
            occurrences_list.append(result)

    return occurrences_list


def search_by_word(word, instance):

    occurrences_list = []
    for item in instance:
        result = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line_index, line_word in enumerate(item["linhas_do_arquivo"], 1):
            occurrences = sliding_window(line_word, len(word))
            if deque(word) in occurrences:
                occurrence = {
                    "linha": line_index,
                    "conteudo": line_word,
                }
                result["ocorrencias"].append(occurrence)

        if result["ocorrencias"]:
            occurrences_list.append(result)

    print(occurrences_list)

    return occurrences_list
