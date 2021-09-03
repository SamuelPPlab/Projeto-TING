class Queue:
    first_element = 0

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self.data:
            return self.data.pop(self.first_element)
        return None

    def search(self, index):
        """Aqui irá sua implementação"""
        self_indexes = self.__len__()
        if index < 0 or index >= self_indexes:
            raise IndexError
        return self.data[index]
