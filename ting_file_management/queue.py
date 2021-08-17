from ting_file_management.deque import Deque


class Queue:
    def __init__(self):  # faz um push dos elementos da fila
        self.__data = Deque()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        return self.__data.push_back(value)  # Enfileirar

    def dequeue(self):
        return self.__data.pop_front()  # Desinfileirar

    def search(self, index):
        return self.__data.find_element(index)
