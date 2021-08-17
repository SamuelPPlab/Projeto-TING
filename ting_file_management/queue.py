class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.insert(self.FIRST_ELEMENT, value)

    def dequeue(self):
        return self._data.pop()

    def search(self, index):
        bool = self._data[index]
        if bool:
            return self._data[len(self) - 1 - index]
        else:
            raise IndexError
