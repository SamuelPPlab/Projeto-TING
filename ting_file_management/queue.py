import sys


class Queue:
    def __init__(self):
        self.my_queue = []
        self.my_file_names = set()

    def __len__(self):
        return len(self.my_queue)

    def enqueue(self, value):
        self.my_queue.append(value)
        print(type(value) == 'dict')
        if type(value) is dict:
            print(value['nome_do_arquivo'])
            print('olaRRRRRRRRRR')
            self.my_file_names.add(value['nome_do_arquivo'])
        else:
            print('erro')

    def dequeue(self):
        if type(self.my_queue[0]) is dict:
            self.my_file_names.discard(self.my_queue[0]['nome_do_arquivo'])
        return self.my_queue.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        try:
            return self.my_queue[index]
        except IndexError:
            print("Index does not exist", file=sys.stderr)
            raise
