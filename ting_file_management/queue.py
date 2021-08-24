from ting_file_management.deque import Deque


class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = Deque()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self._data.push_back(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self._data.pop_front()

    def search(self, index):
        """Aqui irá sua implementação"""
        if (index < 0):
            raise IndexError
        else:
            return self._data.find_element_by_index(index)
