class Queue:
    def __init__(self):
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

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
