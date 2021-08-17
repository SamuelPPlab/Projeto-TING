class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        """Insert the value at the end of the list"""
        self._data.append(value)

    def dequeue(self):
        """Remove the value at the end of the list"""
        return self._data.pop(0)

    def search(self, index):
        """Search a element in the list through the index"""
        if index < 0:
            raise IndexError()
        return self._data[index]

    def index(self, value):
        """Search the index of the element in the queue"""
        return self._data.index(value)
