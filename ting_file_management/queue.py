class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.__data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.__data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.__data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self.__data:
            return self.__data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        """Aqui irá sua implementação"""
        if index > len(self) or index < 0:
            raise IndexError
        else:
            return self.__data[index]
