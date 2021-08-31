from ting_file_management.file_management import txt_importer
from ting_file_management.file_process import get_file_report


def get_lines_with_word(lines, word):
    ocurrencies = []
    for index in range(len(lines)):
        if word.lower() in lines[index].lower():
            ocurrencies.append({'linha': index + 1})
    return ocurrencies or False


def exists_word(word, instance):
    word_search_report = []
    for i in range(len(instance)):
        file_report = get_file_report(instance.search(i), instance)
        file_lines = list(txt_importer(file_report["nome_do_arquivo"]))
        match = get_lines_with_word(file_lines, word)

        if not match:
            return []
        word_search_report.append({
            "palavra": word,
            "arquivo": file_report["nome_do_arquivo"],
            "ocorrencias": match
        })

    return word_search_report


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
