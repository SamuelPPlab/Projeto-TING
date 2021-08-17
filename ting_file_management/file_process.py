import sys


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


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    removido = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {removido} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        return instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")


project = Queue()
print(process("statics/arquivo_teste.txt", project))
print(process("statics/arquivo_teste.txt", project))
