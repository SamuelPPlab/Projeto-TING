class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Deque(" + ", ".join(map(lambda x: str(x), self._data)) + ")"

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(0)
        return None

    def xablau(self):
        for item in range(len(self._data)):
            print(item, self._data[item])

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]


