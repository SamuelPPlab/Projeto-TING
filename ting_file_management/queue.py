class Queue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(0)

    def search(self, index):
        try:
            if index == -1:
                raise
            return self._data[index]
        except:
            print('O erro IndexError foi lançado')
            raise IndexError
