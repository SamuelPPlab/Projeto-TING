class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError()
        return self.data[index]

    def index(self, value):
        return self.data.index(value)
