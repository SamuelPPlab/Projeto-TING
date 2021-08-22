class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]

        else:
            raise IndexError

    def is_used_file(self, file):
        for item in self._data:
            if item['nome_do_arquivo'] == file:
                return True

            return False
