class Queue:
    def __init__(self):
        self.values = []

    def __len__(self):
        return len(self.values)

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        return self.values.pop(0)

    def search(self, index):
        if (index >= len(self.values) or index < 0):
            raise IndexError
        return self.values[index]

    def search_by_value(self, value):
        return self.values.count(value)
