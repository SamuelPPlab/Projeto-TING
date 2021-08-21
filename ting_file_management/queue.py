from ting_file_management.file_management import txt_importer
import sys


class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def search(self, index):
        size = self.__len__()
        if index < 0 or size == 0:
            raise IndexError()
        return self.data[index]


if __name__ == "__main__":
    queue = Queue()

    def process(path_file, instance):
        process_file = {}
        file = txt_importer(path_file)
        process_file['nome_do_arquivo'] = path_file
        process_file['qtd_linhas'] = len(file)
        process_file['linhas_do_arquivo'] = file
        instance.enqueue(process_file)
        sys.stdout.write(f"{process_file}\n")
        return process_file

    def remove(instance):
        if instance.__len__() == 0:
            return sys.stdout.write("Não há elementos\n")
        name_file = instance.dequeue()
        return name_file.get('nome_do_arquivo')
        # return sys.stdout.write(f" Arquivo {name_file} removido com sucesso")

    process('arquivo_teste.txt', queue)
    print(remove(queue));