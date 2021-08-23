class Queue:

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):  # Adds an item to the queue
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):  # Removes an item from the queue
        """Aqui irá sua implementação"""
        oldest = self._data[0]
        del self._data[0]
        return oldest

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self._data):
            raise IndexError()

        return self._data[index]

# Referencia: arthur-massaini-project-ting (#63) e
# https://www.geeksforgeeks.org/queue-in-python/
