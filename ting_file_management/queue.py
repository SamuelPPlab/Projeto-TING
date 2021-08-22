class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if (len(self.queue) - 1) > index < 0:
            raise IndexError
        return self.queue[index]


""" Aula 38.1 course """
