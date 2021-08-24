# código retirado do course da trybe, dia 38.2.Tópico:
# Implementação de uma deque utilizando Python


class Deque:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push_back(self, value):
        self._data.append(value)

    def pop_front(self):
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def find_element_by_index(self, index):
        return self._data[index]
