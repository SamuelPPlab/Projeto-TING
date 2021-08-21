class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.q = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.q)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.q.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        value = self.q[0]
        self.q = self.q[1:]
        return value

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index > len(self):
            raise IndexError()
        return self.q[index]
