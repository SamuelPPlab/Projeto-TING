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
        raise IndexError()

    def search(self, index):
        length = self.__len__()
        if length == 0 or index < 0:
            raise IndexError()
        return self._data[index]

    def file_already_exists(self, value):
        for file in self._data:
            if file == value:
                return True
        return False
