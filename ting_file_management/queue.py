class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data: list = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self._data:
            return self._data.pop(0)

        return None

    def search(self, index):
        """Aqui irá sua implementação"""
        if not self._data or index < 0 or index > len(self._data) - 1:
            raise IndexError()
        return self._data[index]

    def get_data(self):
        return self._data
