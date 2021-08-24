class Queue:
    def __init__(self):
        self.__queueItems = []

    def __len__(self):
        return len(self.__queueItems)

    def enqueue(self, value):
        self.__queueItems.append(value)

    def dequeue(self):
        return self.__queueItems.pop(0)

    def search(self, index):
        if index < 0 or index >= self.__len__():
            raise IndexError()
        return self.__queueItems[index]
