class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        if value not in self._data:
            self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        item = self._data[0]
        del self._data[0]
        return item

    def search(self, index):
        """Aqui irá sua implementação"""
        try:
            if index > len(self._data) or index <= -1:
                raise IndexError
            else:
                return self._data[index]
        except IndexError:
            raise IndexError

# # Testes manuais:
# run = Queue()
# run.enqueue(1)
# run.enqueue(2)
# run.enqueue(3)
# print(run._data)
# run.dequeue()
# print(run._data)
# print(run.search(0))
