class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.data.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index in range(len(self.data)):
            return self.data[index]
        else:
            raise IndexError
