class Queue:

    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        FIRST_ELEMENT = 0
        return self.queue.pop(FIRST_ELEMENT)

    def search(self, index):
        if index in range(self.__len__()):
            return self.queue[index]
        raise IndexError("Index inválido")
