class Queue:
    def __init__(self):
        self._queue = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        if value not in self._queue:
            self._queue.append(value)
            self.__length += 1

    def dequeue(self):
        first_removed = self._queue.pop(0)
        self.__length -= 1
        return first_removed

    def search(self, index):
        if self.__length == 0:
            raise IndexError
        while self._queue:
            if not self._queue[index] or index < 0:
                raise IndexError
            return self._queue[index]
