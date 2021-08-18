class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui, Somente para abrir a PR"""
        self.items = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.items)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.items.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.items.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0:
            raise IndexError(index)
        return self.items[index]
