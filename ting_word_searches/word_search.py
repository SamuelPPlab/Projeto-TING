from ting_file_management.file_management import txt_importer
from ting_file_management.file_process import get_file_report


def get_lines_with_word(lines, word, content):
    ocurrencies = []
    for index in range(len(lines)):
        if word.lower() in lines[index].lower():
            if not content:
                ocurrencies.append({'linha': index + 1})
            else:
                ocurrencies.append({
                    'linha': index + 1,
                    'conteudo': lines[index]
                    })
    return ocurrencies or False


def generate_report(word, instance, content=False):
    word_search_report = []
    for i in range(len(instance)):
        file_report = get_file_report(instance.search(i), instance)
        file_lines = list(txt_importer(file_report["nome_do_arquivo"]))
        match = get_lines_with_word(file_lines, word, content)

        if match:
            word_search_report.append({
                "palavra": word,
                "arquivo": file_report["nome_do_arquivo"],
                "ocorrencias": match
            })

    return word_search_report or []


def exists_word(word, instance):
    return generate_report(word, instance)


def search_by_word(word, instance):
    return generate_report(word, instance, True)
