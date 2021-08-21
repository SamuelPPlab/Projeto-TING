class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def search(self, index):
        size = self.__len__()
        if index < 0 or size == 0:
            raise IndexError()
        return self.data[index]
