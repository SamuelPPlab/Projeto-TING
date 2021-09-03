class Queue:
    first_element = 0
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)
    def dequeue(self):
        """Aqui irá sua implementação"""
        if self._data:
            return self._data.pop(self.first_element)
        return None

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0:
            raise IndexError
        if self._data[index]:
            return self._data[index]
        raise IndexError
