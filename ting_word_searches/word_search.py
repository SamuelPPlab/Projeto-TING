def exists_word(word, instance):
    list_phases = instance.display_queue()
    report_completed = list()

    for resume in list_phases:
        occurrences = list()
        for index, line in enumerate(resume["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})
        report = {
            "palavra": word,
            "arquivo": resume["nome_do_arquivo"],
            "ocorrencias": occurrences,
        }
        if occurrences:
            report_completed.append(report)
    return report_completed


def search_by_word(word, instance):
    list_phases = instance.display_queue()
    report_completed = list()

    for resume in list_phases:
        occurrences = list()
        for index, line in enumerate(resume["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1, "conteudo": line})
        report = {
            "palavra": word,
            "arquivo": resume["nome_do_arquivo"],
            "ocorrencias": occurrences,
        }
        if occurrences:
            report_completed.append(report)
    return report_completed


# my_list = Queue()
# processed_content = {
#         "nome_do_arquivo": "arquivo.txt",
#         "qtd_linhas": 3,
#         "linhas_do_arquivo": ["Aqui contem um Pedro."],
#     }
# # processed_content2 = {
# #         "nome_do_arquivo": "outro_arquivo.txt",
# #         "qtd_linhas": 3,
# #         "linhas_do_arquivo": ["chamado Pedro.", "Aqui tambem tem"],
# #     }
# my_list.enqueue(processed_content)
# # my_list.enqueue(processed_content2)
# print(search_by_word('pedro', my_list))
