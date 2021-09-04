class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(self.FIRST_ELEMENT)

    def search(self, index):
        if index not in range(self.__len__()):
            raise IndexError
        return self.data[index]
