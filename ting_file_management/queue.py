class Queue:
    def __init__(self):
        self.queue = list()
        self.INITIAL_INDEX = 0

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        if value not in self.queue:
            self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(self.INITIAL_INDEX)
        return None

    def search(self, index):
        if index < self.INITIAL_INDEX or index > len(self) - 1:
            raise IndexError()
        return self.queue[index]
