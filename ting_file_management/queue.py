class Queue:
    def __init__(self):
        self.lista = list()
        self.tamanho = 0

    def __len__(self):
        return len(self.lista)

    def enqueue(self, value):
        self.lista.append(value)

    def dequeue(self):
        return self.lista.pop(0)

    def search(self, index):
        retorno = None
        if index < 0:
            raise IndexError()
        try:
            retorno = self.lista[index]
        except IndexError:
            raise IndexError("list index out of range")
        return retorno


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.search(0))
    print(len(q))
    q.dequeue()
    print(q.search(0))
