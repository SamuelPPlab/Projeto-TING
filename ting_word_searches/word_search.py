from ting_file_management.file_management import txt_importer
from ting_file_management.file_process import load_queue


def analyze_line(line, index, search=False):
    result = {"linha": index + 1}
    if search:
        result["conteudo"] = line
    return result


def exists_word(word, instance, search=False):
    occurrences = []
    for path_file in load_queue(instance):
        analyze = {}
        analyze["palavra"] = word
        analyze["arquivo"] = path_file

        file = txt_importer(path_file)
        occurrences_lines = [
            analyze_line(line, index, search)
            for index, line in enumerate(file)
            if word.lower() in line.lower()
        ]

        analyze["ocorrencias"] = occurrences_lines

        if len(analyze["ocorrencias"]) > 0:
            print(analyze)
            occurrences.append(analyze)

    return occurrences


def search_by_word(word, instance):
    return exists_word(word, instance, True)
