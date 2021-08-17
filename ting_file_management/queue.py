class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        if value not in self.data:
            return self.data.append(value)

    def dequeue(self):
        value = self.data[0]
        del self.data[0]
        return value

    def search(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError
