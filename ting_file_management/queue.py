class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)

    def search(self, index):
        if index not in range(self.__len__()):
            raise IndexError('Invalid index')

        return self.data[index]
