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
        if index < 0:
            raise IndexError
        if self.data[index]:
            return self.data[index]
        raise IndexError
