def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        file = instance.search(index)
        word_found = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_found["ocorrencias"].append({"linha": index + 1})
        if len(word_found["ocorrencias"]):
            result.append(word_found)
    return result


def search_by_word(word, instance):
    result = exists_word(word, instance)
    if len(result):
        for idx_file in range(len(instance)):
            file = instance.search(idx_file)
            file_lines = file["linhas_do_arquivo"]
            listed_lines = result[idx_file]["ocorrencias"]
            for idx_line, line in enumerate(listed_lines):
                str_idx = line.get("linha") - 1
                listed_lines[idx_line]["conteudo"] = file_lines[str_idx]
            result[idx_file]["ocorrencias"] = listed_lines
    return result
