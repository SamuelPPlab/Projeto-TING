class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._value = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._value)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        if value not in self._value:
            self._value.append(value)
        else:
            raise NameError()

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self._value.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if (index < 0) or (index > len(self._value)):
            raise IndexError()

        return self._value[index]
