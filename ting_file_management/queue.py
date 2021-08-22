class Queue:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def enqueue(self, value):
        self.stack.append(value)

    def dequeue(self):
        return self.stack.pop(0)

    def search(self, index):
        if index < 0 or not bool(self.stack[index]):
            raise IndexError()
        return self.stack[index]
