class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.queue.pop(0)

    def search(self, index):
        if index not in range(len(self.queue)):
            raise IndexError
        else:
            return self.queue[index]

# if __name__ == "__main__":
#     lista = Queue()
#     lista.enqueue(10)
#     lista.enqueue(8)
#     # lista.dequeue()
#     print(lista.search(0))
#     # print(lista.queue)
