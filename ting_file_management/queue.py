class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        is_index_valid = index < len(self.data) and index >= 0
        if is_index_valid:
            return self.data[index]
        else:
            raise IndexError()