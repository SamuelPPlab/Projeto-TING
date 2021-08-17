class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if self.is_empty() or index < 0 or index >= len(self._data):
            raise IndexError()
        value = self._data[index]
        return value

    def is_empty(self):
        return not bool(self.size())

    def size(self):
        return len(self._data)
