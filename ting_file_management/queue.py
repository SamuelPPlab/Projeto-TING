class Queue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue) 

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def search(self, index):
        if index <= len(self._queue) - 1 and index >= 0:
            return self._queue[index]
        else:
            raise IndexError("IndexError")
