class Queue:
    def __init__(self):
        self.files = []

    def __len__(self):
        return len(self.files)

    def enqueue(self, value):
        return self.files.append(value)

    def dequeue(self):
        return self.files.pop(0)

    def search(self, index):
        if index >= 0:
            return self.files[index]
        else:
            raise IndexError
       
