class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if self._data[index] and index >= 0:
            return self._data[index]
        else:
            raise IndexError
