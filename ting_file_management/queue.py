from collections import deque


class Queue:
    def __init__(self, q_size=20):
        self.q = deque(maxlen=q_size)

    def __len__(self):
        return len(self.q)

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        return self.q.popleft()

    def search(self, index):
        if index < 0 or index >= len(self):
            raise IndexError
        return self.q[index]
