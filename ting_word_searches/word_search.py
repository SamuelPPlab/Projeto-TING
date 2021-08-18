import sys


def txt_importer(path_file):
    try:
        with open(path_file, "r", encoding="utf-8") as file:
            content_file = []
            if path_file.split('.')[-1] == 'txt':
                for readline in file:
                    content_file.append(readline.rstrip('\n'))
                return content_file
            sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Deque(" + ", ".join(map(lambda x: str(x), self._data)) + ")"

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(0)
        return None

    def xablau(self):
        for item in range(len(self._data)):
            print(item, self._data[item])

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError()



def process(path_file, instance):
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None
    arquivo = txt_importer(path_file)
    retorno = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(arquivo),
        "linhas_do_arquivo": arquivo
    }
    sys.stdout.write(f"{retorno}\n")
    return instance.enqueue(retorno)


def exists_word(word, instance):
    for item in range(len(instance)):
        data = instance.search(item)["linhas_do_arquivo"]
        retorno = find_word(word, data, instance, item)
    return retorno

def find_word(word, data, instance, item):
    """Aqui irá sua implementação"""
    result = []
    index = 0
    lista = []
    for linha in data:
        index += 1
        resultado = linha.lower().find(word.lower())
        if resultado >= 0:
            lista.append({"linha": index})
    result.append(
        {
            "palavra": word,
            "arquivo": instance.search(item)["nome_do_arquivo"],
            "ocorrencias": lista,
        }
    )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    result = []
    data = instance.search(0)
    print(data)
    match = re.search(word, data["linhas_do_arquivo"], re.IGNORECASE)
    print(match)
    result.append(
        {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": [
                {
                    "linha": data["qtd_linhas"],
                    "conteudo": data["linhas_do_arquivo"],
                }
            ],
        }
    )
    if match:
        return result
    else:
        return []



project = Queue()
# print(project)
process("statics/nome_pedro.txt", project)
print(exists_word("Pedro", project))