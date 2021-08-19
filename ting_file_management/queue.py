class Queue:
    def __init__(self):
        self.queue_list = list()
        self.__length = 0

    def __len__(self):
        return len(self.queue_list)

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        if len(self) > 0:
            returned_value = self.queue_list[0]
            self.queue_list = self.queue_list[1:]
        return returned_value

    def search(self, index):
        value_returned = ""
        for item_index, item in enumerate(self.queue_list):
            if item_index == index:
                value_returned = item
        if index < 0 or value_returned == "":
            raise IndexError
        return value_returned
