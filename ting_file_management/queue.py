class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        if value not in self._data:
            self._data.append(value)

    def dequeue(self):
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        try:
            if index <= -1 or index > len(self._data):
                raise IndexError
            else:
                return self._data[index]
        except IndexError:
            raise IndexError
