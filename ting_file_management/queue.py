import sys


class Queue:
    def __init__(self):
        self.my_queue = []

    def __len__(self):
        return len(self.my_queue)

    def enqueue(self, value):
        self.my_queue.append(value)

    def dequeue(self):
        return self.my_queue.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        try:
            return self.my_queue[index]
        except IndexError:
            print(file=sys.stderr)
            raise
