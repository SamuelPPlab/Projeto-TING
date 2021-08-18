class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.__queue = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.__queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.__queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.__queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 <= index < len(self.__queue):
            return self.__queue[index]

        raise IndexError
