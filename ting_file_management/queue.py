class Queue:
    def __init__(self):
        self.my_list = list()

    def __len__(self):
        return len(self.my_list)

    def enqueue(self, value):
        self.my_list.append(value)

    def dequeue(self):
        firs_item = self.my_list[0]
        del(self.my_list[0])
        return firs_item

    def search(self, index):
        try:
            return self.my_list[index]
        except IndexError:
            raise IndexError
