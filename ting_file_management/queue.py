class Queue:
    def __init__(self):
        self.__queue = []
        self.__item_position = 0

    def __len__(self):
        return len(self.__queue)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__queue[self.__item_position]
            self.__item_position += 1
            return item
        except IndexError:
            raise StopIteration

    def enqueue(self, value):
        if value in self.__queue:
            return
        self.__queue.append(value)

    def dequeue(self):
        return self.__queue.pop(0)

    def search(self, index):
        if index >= 0 and index <= len(self.__queue):
            return self.__queue[index]
        else:
            raise IndexError
