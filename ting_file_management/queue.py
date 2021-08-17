class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        """Aqui irá sua implementação"""
        try:
            if index <= len(self._data) - 1 and index >= 0:
                return self._data[index]
            else:
                raise IndexError("IndexError")
        except IndexError:
            raise IndexError
