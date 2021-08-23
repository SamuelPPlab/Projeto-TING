class Queue:
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        return self.__data.pop(0)

    def search(self, index):
        if index > len(self.__data) - 1:
            raise IndexError
        if index < 0 :
            raise IndexError
        return self.__data[index]
