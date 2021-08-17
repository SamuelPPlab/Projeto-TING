import re
from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    """Return the lines where the word exists"""
    result = [
        {
            "palavra": f"{word}",
            "arquivo": f"{instance.search(0)}",
            "ocorrencias": [],
        }
    ]
    for index, line in enumerate(txt_importer(instance.search(0))):
        if re.search(f"(?i){word}", line):
            result[0]["ocorrencias"].append({"linha": int(f"{index + 1}")})
    if result[0]["ocorrencias"]:
        return result
    return []


def search_by_word(word, instance):
    """Return the lines with the content where the word exists"""
    result = exists_word(word, instance)
    if result:
        for index, line in enumerate(txt_importer(instance.search(0))):
            if index == result[0]["ocorrencias"][index]["linha"] - 1:
                result[0]["ocorrencias"][index]["conteudo"] = line
    return result
