from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        first_of_queue = self.queue[0]
        self.queue.popleft()
        return first_of_queue

    def search(self, index):
        value = self.queue[index]
        if value is None or index < 0:
            raise IndexError

        return value
