class Queue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        if value not in self._queue:
            self._queue.append(value)

    def dequeue(self):
        item = self._queue[0]
        del self._queue[0]
        return item

    def search(self, index):
        if 0 <= index < len(self._queue):
            return self._queue[index]
        raise IndexError
