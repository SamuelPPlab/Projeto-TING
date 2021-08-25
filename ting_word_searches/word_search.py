from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    result = []

    for file_path in instance.queue:
        file_occurrences = {
            'palavra': word,
            'arquivo': file_path,
            'ocorrencias': []
        }

        for index, line in enumerate(txt_importer(file_path)):
            if line.lower().find(word.lower()) > -1:
                file_occurrences['ocorrencias'].append({'linha': index + 1})

        result.append(file_occurrences)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
