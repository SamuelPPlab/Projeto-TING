class Queue:
    def __init__(self):
        self.listItens = list()

    def __len__(self):
        return len(self.listItens)

    def enqueue(self, value):
        self.listItens.append(value)

    def dequeue(self):
        return self.listItens.pop(0)

    def search(self, index):
        if not self.listItens[index] or index < 0:
            raise IndexError
        return self.listItens[index]

    def itemNotExists(self, item):
        if item not in self.listItens:
            return True
        else:
            return False
