class Deque:  # Código "Universal apresentado na aula 38.2"
    FIRST_ELEMENT = 0  # Guardião da posição do elemento

    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)  # Tamanho da lista

    def __str__(self):
        return f"Deque( {','.join(str(x) for x in self.__data)})"
        # Imprimir fila como string

    def find_element(self, index):
        if index > len(self) or index < 0:
            raise IndexError
        else:
            return self.__data[index]

    def push_front(self, value):
        self.__data.insert(self.FIRST_ELEMENT, value)

    def push_back(self, value):
        self.__data.append(value)

    def pop_front(self):
        if self.__data:
            return self.__data.pop(self.FIRST_ELEMENT)
        return None

    def pop_back(self):
        if self.__data:
            return self.__data.pop()
        return None

    def peek_front(self):
        if self.__data:
            return self.__data[self.FIRST_ELEMENT]
        return None

    def peek_back(self):
        if self.__data:
            return self.__data[len(self) - 1]
        return None

    def clear(self):
        self.__data.clear()
