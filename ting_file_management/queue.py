class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = list()
        self.INITIAL_INDEX = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        if value not in self.queue:
            self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
