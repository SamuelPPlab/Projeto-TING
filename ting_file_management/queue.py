class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def remove_first(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def dequeue(self):
        if self._data:
            return self._data.pop(0)
        return None

    def search(self, index):
        length = self.__len__()
        if length == 0 or index < 0:
            raise IndexError()
        return self._data[index]
