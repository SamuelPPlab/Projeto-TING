class Queue:
    def __init__(self):
        self.lista = []

    def __len__(self):
        return len(self.lista)

    def enqueue(self, value):
        return self.lista.append(value)

    def dequeue(self):
        return self.lista.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError

        return self.lista[index]
