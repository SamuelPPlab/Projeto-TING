from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    data = instance.get_data()

    output = list()

    for file in data:
        file_data = txt_importer(file)

        count = list()

        for index, line in enumerate(file_data):
            if word in line:
                count.append({'linha': index + 1})

        if len(count) > 0:
            output.append({
                'palavra': word,
                'arquivo': file,
                'ocorrencias': count
            })

    return output


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
