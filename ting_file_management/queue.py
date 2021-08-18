class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        info = self.data[0]
        del self.data[0]
        return info

    def search(self, index):
        if index <= len(self.data) - 1 and index >= 0:
            return self.data[index]
        raise IndexError()

    def get(self):
        return self.data
