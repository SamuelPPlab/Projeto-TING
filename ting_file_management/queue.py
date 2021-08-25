class Queue:
    def __init__(self):
        self.array = list()

    def __len__(self):
        return len(self.array)

    def enqueue(self, value):
        # insert_last
        return self.array.append(value)

    def dequeue(self):
        # remove_last
        array_dequeued = self.array
        del array_dequeued[-1]
        return array_dequeued

    def search(self, index):
        # get_element_at
        if index < 0:
            raise IndexError()
        return self.array[index]