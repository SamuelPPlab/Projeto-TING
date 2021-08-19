class Queue:
    # auxílio exercicios dia 2 bloco 38
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.insert(self.FIRST_ELEMENT, value)

    def dequeue(self):
        if self._data:
            return self._data.pop()
        return None

    def search(self, index):
        if index < 0 or index > len(self) - 1:
            raise IndexError
        return self._data[::-1][index]
