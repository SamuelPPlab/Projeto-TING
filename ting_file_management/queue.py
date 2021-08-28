class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.insert(self.FIRST_ELEMENT, value)

    def dequeue(self):
        if self._data:
            return self._data.pop()
        return None

    def search(self, index):
        if self._data:
            return self._data[len(self._data) - 1 - index]
        raise(IndexError)
