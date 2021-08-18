class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        if value not in self.data:
            self.data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        item = self.data[0]
        del self.data[0]
        return item

    def search(self, index):
        """Aqui irá sua implementação"""
        try:
            if index > len(self.data) or index <= -1:
                raise IndexError
            else:
                return self.data[index]
        except IndexError:
            raise IndexError


# # Testes manuais:
# run = Queue()
# run.enqueue(1)
# run.enqueue(2)
# run.enqueue(3)
# print(run.data)
# run.dequeue()
# print(run.data)
# print(run.search(0))
