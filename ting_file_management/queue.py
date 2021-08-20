class Queue:
    def __init__(self):
        self.result = []

    def __len__(self):
        lengthResult = len(self.result)
        return lengthResult

    def enqueue(self, value):
        self.result.append(value)

    def dequeue(self):
        return self.result.pop(0)

    def search(self, index):
        lengthRes = self.__len__()
        if index < 0 or lengthRes == 0:
            raise IndexError()
        return self.result[index]
