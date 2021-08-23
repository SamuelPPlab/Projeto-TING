class Queue:
    def __init__(self):
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

    def enqueue(self, value):
        # source of ignore yet existent name
        # https://github.com/tryber/sd-07-project-ting/
        # commit/a63c2a96d1564a3e032b979f28b3a06a7c085294
        if value in self.__queue:
            return
        self.__queue.append(value)

    def dequeue(self):
        to_remove = self.__queue[:1][0]
        self.__queue.remove(to_remove)
        return to_remove

    def search(self, index):
        if (index >= 0):
            return self.__queue[index]
        raise IndexError
