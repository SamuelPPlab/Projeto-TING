class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        is_value = self._data[0]
        del self._data[0]
        return is_value

    def search(self, index):
        """Aqui irá sua implementação"""
        print(index)
        if self._data[index] and index >= 0:
            return self._data[index]
        else:
            raise IndexError
