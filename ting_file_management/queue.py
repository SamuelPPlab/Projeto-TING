class Queue:
    def __init__(self):
        self.array = list()

    def __len__(self):
        len(self.array)

    def enqueue(self, value):
        # insert_last
        self.array.insert(value)

    def dequeue(self):
        # remove_last
        self.array = self.array[:1]

    def search(self, index):
        # get_element_at
        if index < 0 or not index:
            raise IndexError()
        self.array[index]