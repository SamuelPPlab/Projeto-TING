class Queue:
    def __init__(self):
        self._data = []

    def __str__(self):
        return f"List(len={self.__len__()}, value={self._data})"

    def display_queue(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if index >= self.__len__() or index < 0:
            raise IndexError
        return self._data[index]


# fila = Queue()
# fila.enqueue(1)
# fila.enqueue(2)
# fila.enqueue(3)
# fila.dequeue()
# print(fila.search(1))
# print(fila)
