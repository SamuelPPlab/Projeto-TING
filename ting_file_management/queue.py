class Queue:
    def __init__(self):
        self.queue = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.queue.append(value)
        self.__length += 1
        return value

    def dequeue(self):
        first_removed = self.queue[0]
        self.__length -= 1
        return first_removed

    def search(self, index):
        if self.__length == 0:
            raise IndexError
        while self.queue:
            if not self.queue[index] or index < 0:
                raise IndexError
            return self.queue[index]

    def get(self):
        return self.data
