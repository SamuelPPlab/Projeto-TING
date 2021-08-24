class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        head = self._data[0]
        self._data.remove(head)
        return head

    def search(self, index):
        min = index < 0
        max = index >= len(self._data)
        if min or max:
            raise IndexError()

        return self._data[index]
