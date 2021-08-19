def exists_word(word, instance):
    result = []
    for item in instance.queue:
        for line in item["linhas_do_arquivo"]:
            # LER O README, TAVA MUITO CLARO QUE ERA INSENSITIVE E
            # VOCÊ PERDEU MAIS DE HORA TENTANTANDO FAZER ERRADO
            if word.lower() in line.lower():
                result.append({"linha": instance.queue.index(item) + 1})
            if not result:
                return []
        return [{
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": result,
        }]


def search_by_word(word, instance):
    result = []
    for item in instance.queue:
        for line in item["linhas_do_arquivo"]:
            # LER O README, TAVA MUITO CLARO QUE ERA INSENSITIVE E
            # VOCÊ PERDEU MAIS DE HORA TENTANTANDO FAZER ERRADO
            if word.lower() in line.lower():
                result.append(
                    {"linha": instance.queue.index(item) + 1,
                     "conteudo": line})
            if not result:
                return []
        return [{
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": result,
        }]
